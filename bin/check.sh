#!/bin/bash
path=/var/log/gpt_wechat/

check_process() {
  process=`ps aux | grep main.py | grep -v grep`;
  if [[ "$process" == "" ]]
  then
      cd /opt/wechat/gongzhonghao/gpt_wechat/
      python3 main.py
  fi
}

start_process() {
  check_process
}

stop_process() {
  process=`ps aux | grep main.py | grep -v grep`;
  if [[ "$process" == "" ]]
  then
      cd /opt/wechat/gongzhonghao/gpt_wechat/
      python3 main.py
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