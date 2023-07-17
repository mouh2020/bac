from bs4 import BeautifulSoup
from .requests_handler import make_request

class Result : 
    def __init__(self,matricule,code,brute_force=None) : 
        self.html_code = make_request(matricule,code)

    def __valid_result_page(self) : 
        if "الشعبة" in self.html_code : 
            return True
        
    def check_condidate_success(self) : 
        if self.__valid_result_page() and "ألف مبروك" in self.html_code :
            return True
        
    def condidate_result_json(self) : 
        soup = BeautifulSoup(self.html_code,features='lxml')
        keys_tags = soup.find_all('td',{'width':"30%"})
        values_tags = soup.find_all('td',{'width':"70%"})
        student_infos = {}
        for key,value in zip(keys_tags,values_tags) : 
            student_infos [key.text.replace(' : ',"")] = value.text.strip()
        return student_infos



