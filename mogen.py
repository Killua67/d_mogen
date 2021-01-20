# -*- coding: utf-8 -*-
# @Time       : 2021/1/6 15:41 
# @Author     : Killua
# @Email      : killua_67@163.com
# @File       : mogen.py
# @Description: 摩根太平洋对冲基金
# @Software   : PyCharm
import re
import traceback
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.bloomberg.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'bbAbVisits=; __sppvid=7f8f5acf-f9c3-496f-a907-d25c574bb286; _sp_krux=false; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXQGQlksAJ3zQ2mdAAAA; _sp_v1_uid=1:580:5eb098a8-c8e5-4f3a-932c-bdf16120a2eb; _sp_v1_lt=1:; _sp_v1_csv=null; _sp_v1_opt=1:; ccpaUUID=3e63fc89-2d84-493e-8825-1bcef14b95b9; dnsDisplayed=true; ccpaApplies=true; signedLspa=false; bbgconsentstring=req1fun1pad1; _gcl_au=1.1.1452248761.1609917616; bdfpc=004.6253672927.1609917616029; _ga=GA1.2.1021278852.1609917631; _gid=GA1.2.1153649072.1609917631; _rdt_uuid=1609917632332.e24982e5-9863-4523-ab3f-3d0138f1271d; trc_cookie_storage=taboola%2520global%253Auser-id%3D20c94ea2-b0bd-40d9-ae3a-ae188a8ab71e-tuct6828cec; _pxvid=aadbf182-4fef-11eb-b399-0242ac120011; _fbp=fb.1.1609917667978.2068005620; _user-status=anonymous; __gads=ID=3a1e97411d08dc57:T=1609917683:S=ALNI_MZ78acvCS6PqoYHSv2atesHnBHmTg; _reg-csrf=s%3AnmsBfgJw1ZqOlakrEntmi61j.fig6htO7gU9DkMqs%2FwqTBGrvc4IXanz%2F%2BCPs4RoBfPQ; agent_id=c1bbcd5a-9d8c-42b7-8f68-745ef234ca37; session_id=bdec88dc-cb9f-4dc9-9795-e37ebdb508f9; session_key=fe8bc2561392235561c50b7de66ee67dd9e670df; _cc_id=63b48d387656e3fbbe4c4487e357ed4f; _pbjs_userid_consent_data=3524755945110770; _pubcid=381b7528-a99d-41a7-ad7d-275bc28dd4ef; cto_bidid=rDRHKl84MU1qUlc3OERRaG1yanJzVWI1Tkp4UzRic1dqcDFMZmtvNEQzdE5BVXNMREx0OXVuZHZJcmNxZ2RTdW1IbHpsam1qNm0lMkJOOGUlMkJkbVIxRWpkWGdhYXclM0QlM0Q; cto_bundle=1F1q119DNWM0aVFSeEM0NkVFUHRzeCUyRjJQWDJiMnVsMEdMNGZkZWl3SzVuREtCZGtuQXNOaGdBTDRzZGtTdWZ2YU92MCUyQlJhVFpCTG1tWnN1MXQ3YmVmSklXdzQ0bUlLd09wQWxyY0Z3TlEwUEJNbnYlMkIwZkFkVWxpbFZmYXhQbUkwaUhtMg; pbjs-unifiedid=%7B%22TDID%22%3A%22a8105b85-9c7b-4d7c-9145-3a2b7554fd64%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222020-12-06T07%3A28%3A12%22%7D; bb_geo_info={"country":"US","region":"US","cityId":"null","provinceId":"null","fieldD":"colocrossing.com"}|1610522990518; _tb_t_ppg=https%3A//www.bloomberg.com/quote/JFPTECI%3AHK; __tbc=%7Bjzx%7Dt_3qvTkEkvt3AGEeiiNNgOntaanefgtJcAmvU7YFbtl7Ttc7crb7omcv_tc_0QMRuXY6he2p638gOAR-wI8krZGIwKNjPRUH-m6eFNZnK014OVrQj2A_UoJgBgdXtKzOjylU0Z664w9lha1BgkmqDg; __pat=-18000000; _li_dcdm_c=.bloomberg.com; _lc2_fpi=b1166d620485--01evb9mgs4wedmc12cj1pjnm8h; _scid=89712514-4b01-4ffd-82be-d1499dae105e; _sctr=1|1609862400000; com.bloomberg.player.volume.level=1; _sp_v1_data=2:265834:1609917613:0:9:0:9:0:0:_:-1; consentUUID=d69258bb-32b8-4d1a-b40e-52fed6f915d3; _reg-csrf-token=1BS7r6Eo-ikdaxO5gC4EXhtfkQheQW7qZTrg; _uetsid=a96c87e04fef11eb8482331262e3618a; _uetvid=a96ce7904fef11eb9cebcb3dcc942f04; _tb_sess_r=; __pvi=%7B%22id%22%3A%22v-2021-01-06-15-34-22-815-Y0eGwmcEIMF2DC0O-2d77bc83d7024d40b85069ef7998b1be%22%2C%22domain%22%3A%22.bloomberg.com%22%2C%22time%22%3A1609919577122%7D; xbc=%7Bjzx%7DzZwYcarqSfrvkxzWPwiCJVDYgDaO_8QxudlexC5TE2TF3bRpEKXruyfgWNmAJu6utXAxU3nu_P7H8vmHM_GlxPqto2jHimhQ0XWQ_VKNThmiRW_m1Al7d1idbvr5XiXDGIRS1PK_v-68mjOBKhC56DMxyxmK9dsOxK5ubKDPfhHgSS5iY6uV9xaPo5_5l_2DsFieHAnKPPVSLRY8-xFv5REakeiHyY_z8c5IlNF0znhc7T3EOo2YtAxQetG1ZFRM4fM6xS70FQmrgB-7HnBO6Gbbor8U1NusRqyh3FyD4DY; _px2=eyJ1IjoiMjI0N2FmYjAtNGZmNC0xMWViLWE2NTEtNTczMzExOWI1N2MzIiwidiI6ImFhZGJmMTgyLTRmZWYtMTFlYi1iMzk5LTAyNDJhYzEyMDAxMSIsInQiOjE2MDk5MjAwOTU5NzYsImgiOiJkMTViZDhhYTI1ZTA1Y2I2ZDNmNGMzYTU4ODM1MDMyMDExYzNiNTM5MzM0Njk4N2E5ZjI4NzM2ODUxZDcyOGY5In0=; _px3=8d59d1cd0c5f3d6b1cb113491d12db21bb4728af2a0ca84857a90083372597ca:4Dz326IAIdyNBtBmsg4pTG1BA4j11SGiLW+ff071HfIEKnP4h9NCl5JCVsCGhNpEjE3F0ZLdSh2ls/Nf3OxrOw==:1000:pizww3dWafOrQTf9NBvnCji+FqwUN1KO8XE6grucosBlr+hRdXUh56PAqXAgX6EcuIVRvreQ+SbvPu0Htj/8N73UIvKxgfeqwUiLIP5UV497llhdGwH+RNvDvb4EHkzP99RNi/3wJB3A0b5tPf8hELO1ylwB8ejwIK/Wt6oXwl0=; _pxde=4efebbc00e4991fdcf13311ce759faeae62e3fa2aa21240547293ecf36db40e9:eyJ0aW1lc3RhbXAiOjE2MDk5MTk3OTU5NzcsImZfa2IiOjAsImlwY19pZCI6W119; GED_PLAYLIST_ACTIVITY=W3sidSI6IlBlcUIiLCJ0c2wiOjE2MDk5MTk5NzYsIm52IjoxLCJ1cHQiOjE2MDk5MTk1NTAsImx0IjoxNjA5OTE5OTc2fSx7InUiOiJxQ1AwIiwidHNsIjoxNjA5OTE5OTc1LCJudiI6MCwidXB0IjoxNjA5OTE3OTkxLCJsdCI6MTYwOTkxODkzNn1d',
}
# 忽略警告
requests.packages.urllib3.disable_warnings()
url_host = 'https://www.bloomberg.com'
holding_dict = {}
task = []


def get_holding():
    response = requests.get(url_host + '/quote/JFPTECI:HK', headers=headers, verify=False)
    html = BeautifulSoup(response.text, 'lxml')
    holds = html.find_all('span', text='Fund Top Holdings')
    if len(holds) == 0:
        print('访问频次太高，触发网页脚本检查，请在网页访问进行人机检查后即可再使用')
        return
    for item in holds[0].find_parent().find_parent().children:
        urls = item.find_all('a')
        if len(urls) > 0:
            percentage = item.contents[-1].text[:-1]
            url = urls[0].attrs['href']
            holding_dict[url] = percentage
    # 基金预估
    prices = html.find_all('section', attrs={'class': re.compile('price__')})
    if len(prices) > 0:
        info = prices[0].text
        match = re.findall('[+-].{4}%', info)
        print('基金官方预估涨跌：' + match[0])


def up_down(url_item, lost, retry):
    current = 0
    # 异常重试
    while current < retry:
        try:
            response = requests.get(url_host + url_item[0], headers=headers, verify=False)
            html = BeautifulSoup(response.text, 'lxml')
            prices = html.find_all('section', attrs={'class': re.compile('price__')})
            company_name = html.find_all('h1', attrs={'class': re.compile('companyName__')})
            if len(prices) > 0 and len(company_name) > 0:
                info = prices[0].text
                match = re.findall('[+-].{4,5}%', info)
                if len(match) == 0 and info is not None and info != '':
                    ud = '+0'
                else:
                    ud = match[0][:-1]
                evl = eval(url_item[1] + '*(100' + ud + ')*100/' + str(lost))
                print('%s,持仓比例：%s%%,涨跌:%s%%' % (company_name[0].text, url_item[1], ud))
                return evl
            break
        except (requests.exceptions.SSLError, requests.exceptions.ProxyError):
            pass
        except:
            print(traceback.format_exc())
            current += 1
    print('%s 查询异常' % url_item[0])
    return 0


if __name__ == '__main__':
    result = 0.00
    lost = 0
    get_holding()
    if len(holding_dict) > 0:
        for val in holding_dict.values():
            lost += eval(val)
        print('已知总持仓：%s%%' % lost)
        executor = ThreadPoolExecutor(len(holding_dict))
        for item in holding_dict.items():
            task.append(executor.submit(up_down, item, lost, 5))
        for future in as_completed(task):
            result += future.result()
    print('计算预估涨幅：%.3f%%' % (result / 100 - 100))
