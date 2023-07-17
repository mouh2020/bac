from bs4 import BeautifulStoneSoup
import re

class Captcha : 
    
    def __init__(self,page_html) : 
        self.page_html = page_html
        self.soup      = BeautifulStoneSoup(self.page_html,features="lxml")

    def get_captcha_field(self):
        self.captcha_field = self.soup.find(text=lambda text: text and 'كم يساوي' in text).text

    def clean_captcha(self) : 
        self.captcha_field = self.captcha_field.replace('كم يساوي ',"").replace('؟','')

    def extract_operation(self) :
        if "+" in self.captcha_field : 
            self.operation ="addition"
            return
        self.operation ="subtraction"
            
    def extract_operation_numbers(self) :
        if self.operation == "addition" : 
            self.first_number,self.second_number = self.captcha_field.split('+')
            return
        self.first_number,self.second_number = self.captcha_field.split('-')
    def captcha_result(self) : 
        self.first_number = int(self.first_number)
        self.second_number= int(self.second_number)
        if self.operation == "addition" : return self.first_number+self.second_number
        if self.first_number > self.second_number : 
            return self.first_number-self.second_number
        return self.second_number-self.first_number
    
        
 