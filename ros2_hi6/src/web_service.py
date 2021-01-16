import requests
import json
import time
import sys

from datetime import datetime
from threading import Thread

headers = {'Content-Type': 'application/json; charset=utf-8', }
url_head = 'http://192.168.1.250:8888'

class http_client(object):

    def request(self, method_name, url, dict_data, is_urlencoded=True, timeout_seconds=1):
        """Web GET or POST request를 호출 후 그 결과를 dict형으로 반환 """
        method_name = method_name.upper()  # 메소드이름을 대문자로 바꾼다
#        print(method_name + ' : ' + url)
        if method_name not in ('GET', 'POST'):
            raise Exception('method_name is GET or POST plz...')

        if method_name == 'GET':  # GET방식인 경우
            response = requests.get(url=url, params=dict_data, timeout=timeout_seconds)
        elif method_name == 'POST':  # POST방식인 경우
            if is_urlencoded is True:
                response = requests.post(url=url, data=dict_data, \
                                         timeout=timeout_seconds,
                                         headers=headers)
            else:
                response = requests.post(url=url, data=json.dumps(dict_data), \
                                         timeout=timeout_seconds, headers=headers)

        dict_meta = {'status_code': response.status_code, 'ok': response.ok}
        if 'json' in str(response.headers['Content-Type']):  # JSON 형태인 경우
            if (type(json.loads(response.text)) is dict): # JSON 형태인 경우
                return {**dict_meta, **response.json()}
            else:
                return {**dict_meta, **{'text': response.text}}
        else:  # 문자열 형태인 경우
            return {**dict_meta, **{'text': response.text}}

    def request_retry(self, num_retry=2, sleep_seconds=0.5, **kwargs):
        """timeout발생 시 sleep_seconds쉬고 num_retry번 재시도 한다"""
        for n in range(num_retry):
            try:
                return self.request(**kwargs)
            except requests.exceptions.Timeout:
                print(str(n + 1) + ' Timeout')
                time.sleep(sleep_seconds)
                continue
        return None

    def service_request(self, method, url_tail, data, command):
        try:
            url = url_head + url_tail
#            print('service_request : ' + url)
            response = self.request_retry(method_name=method, url=url, dict_data=data, is_urlencoded=True, num_retry=2)
            # GET DATA는 상태창에 표시 하지 않는다.
            if method == "GET":
                return response

            self.stats_log(response, command)

            bRet = False
            if response['ok']:
                bRet = True

            return bRet

        except Exception as ex:
            self.stats_log('No response', command)
            return None

    def stats_log(self, response, command):
        print('%s' % response)

#def main():
    # node = web_service()


#if __name__ == '__main__':
#    main()

