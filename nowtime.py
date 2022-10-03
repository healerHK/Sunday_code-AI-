import datetime
import time
def get_time():
    print("yêu cầu của bạn là gì")
    text=input()
    now = datetime.datetime.now()
    if "giờ" in text:
        print('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        print("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        print("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")
get_time()
