#!/bin/bash
path=/var/log/gpt_wechat/
gpt_path=/opt/wechat/gongzhonghao/gpt_wechat/

check_process() {
  process=`ps aux | grep main.py | grep -v grep| awk '{print $2}'`;
  if [[ "$process" == "" ]]
  then
      echo "gpt_wechat is not running"
      return 1
  else
    echo "gpt_wechat is running, pid is $process"
    return 0
  fi
}

start_process() {
  process=`ps aux | grep main.py | grep -v grep| awk '{print $2}'`;
  if [[ "$process" == "" ]]
  then
      echo "start gpt_chat now"
      cd $gpt_path
      nohup python3 main.py >/dev/null 2>&1
      echo "start gpt_chat success"
  fi
}

stop_process() {
  process=`ps aux | grep main.py | grep -v grep | awk '{print $2}'`;
  if [[ "$process" == "" ]]
  then
    echo "gpt_chat is not running, no need to stop."
  else
    kill -9 "$process"
    echo "stop gpt_chat success, pid:$process"
  fi
}
# 根据参数执行相应操作
case "$1" in
    start)
        start_process
        ;;
    stop)
        stop_process
        ;;
    restart)
        stop_process
        start_process
        ;;
    status)
        check_process
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac

exit 0