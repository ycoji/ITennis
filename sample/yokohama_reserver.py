import argparse
import json
import time
from datetime import datetime as dt
import schedule
import sys
sys.path.append('../')
from ITennis.efficient_tennis_driver import YokohamaTennisDriver


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('config', type=str)
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = json.load(f)

    print(config)
    driver = YokohamaTennisDriver(config['user_id'], config['pass'])

    requests = config['requests']
    for request in requests:
        if request['type'] == "reservation":
            play_time_str = request['param']['date'] + "T" + request['param']['time'] 
            play_time = dt.strptime(play_time_str, '%Y%m%dT%H:%M')
            driver.reserve(place = request['param']['place'], date=play_time)
        else:
            raise ValueError

    """
    while True:
        schedule.run_pending()
        time.sleep(1)
    """

if __name__ == '__main__':
    main()

