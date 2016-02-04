# http://vidaendirecto.com/noticias/votaciones-nominaciones-gran-hermano-vip/
import requests
datos = {
    'action':'polls',
    'poll_106':'354',
    'poll_106_nonce':'cc7c43fa2a',
    'poll_id':'106',
    'view':'process'
}

def send_post(proxyport):

    proxies = { "http": 'http://' + proxyport, "https": 'http://' + proxyport}
    #url = 'http://vidaendirecto.com/noticias/votaciones-nominaciones-gran-hermano-vip/index.php'
    #url = 'http://vidaendirecto.com/wp-admin/admin-ajax.php'
    url = 'http://vidaendirecto.com/index.php'
    try:
        response = requests.post(url, data=datos, proxies=proxies, timeout=20)
        print(response)
        print(proxyport  + ' ...done!')
        return True
    except:
        print(proxyport  + ' ... timeout!')
        return False

with open('proxies.txt', 'r') as f:
    data = f.readlines()

    for line in data:
        send_post(line.strip())




 
