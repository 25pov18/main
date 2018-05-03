import requests

cookies = {
    '_ym_isad': '1',
    'c_r_enc': '1',
    'JSESSIONID_8': '00001QHGuJ4wYo8lBZNqSqYQKIa:19a2vp8dd',
    '__utma': '224553113.1056190029.1525084563.1525084563.1525084563.1',
    '__utmc': '224553113',
    '__utmz': '224553113.1525084563.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none)',
    '_ym_uid': '1525084563957134968',
    'data-popped-ok': '1',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'Referer': 'https://rosreestr.ru/wps/portal/online_request',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'X-Prototype-Version': '1.5.0_rc2',
}

params = (
    ('parentId', '101000000000'),
)

response = requests.get('https://rosreestr.ru/wps/PA_RRORSrviceExtended/Servlet/ChildsRegionController', headers=headers, params=params, cookies=cookies)
print(response.text)



//$(document).ready(function(){

 //  $("#post_btn").click(function(){
 //     $.get(url,function(result){ $("#result").html(result);});
 //  });

//});
/*
var  geturl;

geturl =$.ajax({
            url: url1,
            type: 'POST',
            cookies : {
                '_ym_isad': '1',
                'c_r_enc': '1',
                'JSESSIONID_8': '00001QHGuJ4wYo8lBZNqSqYQKIa:19a2vp8dd',
                '__utma': '224553113.1056190029.1525084563.1525084563.1525084563.1',
                '__utmc': '224553113',
                '__utmz': '224553113.1525084563.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
                '_ym_uid': '1525084563957134968',
                'data-popped-ok': '1'
                    },

            headers: {

                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'Referer': 'https://rosreestr.ru/wps/portal/online_request',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'X-Prototype-Version': '1.5.0_rc2'


            },
            contentType: 'application/json; charset=utf-8',
            success: function () {
               // CallBack(result);
                 alert("done!"+ geturl.getAllResponse());

            },
            error: function (error) {
                console.log('ujdyj: '+result);
               // alert("done!"+ geturl.getAllResponseHeaders());
            }
        });




//requests.get('https://rosreestr.ru/wps/PA_RRORSrviceExtended/Servlet/ChildsRegionController?parentId=101000000000', headers=headers, cookies=cookies)




