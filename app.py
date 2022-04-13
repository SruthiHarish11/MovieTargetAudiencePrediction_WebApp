# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:49:26 2020

@author: Sruthi Harish
"""
from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)

model_one=pickle.load(open("model_one.pkl","rb"))

@app.route('/')
def hello():
    return(render_template('movie.html'))

@app.route('/predict',methods=['GET','POST'])
def predict():
    features=[x for x in request.form.values()]
    #sample=[np.array(features)]
    final_features=[]
    for i in range(0,26):
        if i==0:
            d={'A.R. Murugadoss': 0, 'Aamir Khan': 1, 'Aanad Rai': 2, 'Abhay Chopra': 3, 'Abhisekh Dogra': 4, 'Abhisekh Pathak': 5, 'Abhisekh Sharma': 6, 'Aditya Chopra': 7, 'Amar Kaushik': 8, 'Amit Kapoor': 9, 'Amit Sharma': 10, 'Amit V. Masurkar': 11, 'Anees Bazmee': 12, 'Anubhav Sinha': 13, 'Anurag Basu': 14, 'Anurag Kashyap': 15, 'Anushka Sharma': 16, 'Apoorva Lakhia': 17, 'Ashutosh Gowariker': 18, 'Atul Kasbekar': 19, 'Bhushan Kumar': 20, 'Bhushan Patel': 21, 'Boney Kapoor': 22, 'Dinesh Vijan': 23, 'Ekta Kapoor': 24, 'Farhan Akhtar': 25, 'Firoz A. Nadiadwala': 26, 'Imtiaz Ali': 27, 'Irrfan Khan': 28, 'Jayantilal Gada': 29, 'Kabir Khan': 30, 'Karan Johar': 31, 'Majid Majidi': 32, 'Manish Gupta': 33, 'Milan Luthria': 34, 'Mohit Suri': 35, 'Mudassar Aziz': 36, 'Mukesh Bhatt': 37, 'Namrata Singh Gujral': 38, 'Neeraj Pandey': 39, 'Nikkhil Advani': 40, 'Nitesh Tiwari': 41, 'Prabhu Deva': 42, 'Prashanth Neel': 43, 'R. Balki': 44, 'Radhika Rao': 45, 'Raj Nidimoru': 46, 'Raja Krishna Menon': 47, 'Rajesh Banga': 48, 'Rajkumar Hirani ': 49, 'Rakesh Roshan': 50, 'Ram Gopal Varma': 51, 'Ratnaa Sinha': 52, "Remo D'Souza": 53, 'Robbie Grewal': 54, 'Rohit Shetty': 55, 'Ronnie Screwvala': 56, 'S. S. Rajamouli': 57, 'S. Shankar': 58, 'Sabbir Khan': 59, 'Sajid Nadiadwala': 60, 'Salman Khan': 61, 'Sanjay Gupta': 62, 'Sanjay Leela Bhansali': 63, 'Shaad Ali': 64, 'Shashank Khaitan': 65, 'Shonali Bose': 66, 'Shoojit Sircar': 67, 'Shree Narayan Singh': 68, 'Shreyas Talpade': 69, 'Sriram Raghavan': 70, 'Subhash Kapoor': 71, 'Sujoy Ghosh': 72, "Tony D'Souza": 73, 'Vashu Bhagnani': 74, 'Vidhu Vinod Chopra': 75, 'Vikram Bhatt': 76, 'Vikram Malhotra': 77, 'Vipul Amrutlal Shah': 78, 'Vipul Rawal': 79}
            final_features.append(d[features[0]])
        elif i==1:
            d={'Aamir Khan': 0, 'Aayaush Sharma': 1, 'Abhay Deol': 2, 'Aditya Roy Kapoor': 3, 'Ajay Devgn': 4, 'Akshay Kumar': 5, 'Ali Fazal': 6, 'Amit Sadh': 7, 'Amitabh Bachchan': 8, 'Arjun Kapoor': 9, 'Arjun Rampal': 10, 'Ayushmann Khurana': 11, 'Bhumi Pednekar': 12, 'Diljit Dosanj': 13, 'Emraan Hashmi': 14, 'Farhan Akhtar': 15, 'Gulshan Devaiah': 16, 'Harshvardhan Rane': 17, 'Hrithik Roshan': 18, 'Imran Khan': 19, 'Irrfan Khan': 20, 'Ishaan Khattar': 21, 'Jacky Bhagnani': 22, 'John Abraham': 23, 'K K Menon ': 24, 'Kamal Hasan': 25, 'Karan Kundra': 26, 'Karan Singh Grover': 27, 'Karan Wahi': 28, 'Kartik Aaryan': 29, 'Manav Kaul': 30, 'Nana Patekar': 31, 'Nawazuddin Siddiqui': 32, 'Prabhas ': 33, 'Pulkit Samrat': 34, 'Purab Kohli': 35, 'R. Madhavan': 36, 'Raghav Juyal': 37, 'Rajkumar Rao': 38, 'Ranbir Kapoor': 39, 'Randeep Hooda': 40, 'Ranveer Singh': 41, 'Riddhi Sen': 42, 'Rishi Kapoor': 43, 'Riteish Deshmukh': 44, 'Rohan Mehra': 45, 'Saif Ali Khan': 46, 'Salman Khan': 47, 'Sanjay Dutt': 48, 'Sayani Gupta': 49, 'Shahid Kapoor': 50, 'Shahrukh Khan': 51, 'Shekhar Ravjiani': 52, 'Shreyas Talpade': 53, 'Siddhart Kapoor': 54, 'Siddharth Malhotra': 55, 'Sooraj Pancholi': 56, 'Sparsh': 57, 'Sunny Deol': 58, 'Sushant Singh Rajput': 59, 'Tiger Shroff': 60, 'Varun Dhawan': 61, 'Varun Dhawan ': 62, 'Vicky Kaushal': 63, 'Vidyut Jammwal': 64, 'Vivek Mushran': 65, 'Yash': 66, 'Zayed Khan': 67}
            final_features.append(d[features[1]])
        elif i==2:
            d={'Adah Sharma': 0, 'Aditi Rao Hydari': 1, 'Aisha Sharma': 2, 'Aishwarya Rai': 3, 'Alia Bhatt': 4, 'Amy Jackson': 5, 'Ananya Panday': 6, 'Anjali Patil': 7, 'Anushka Sharma': 8, 'Anushka Shetty': 9, 'Asin': 10, 'Athiya Shetty': 11, 'Bhumi Pednekar': 12, 'Binita Sandhu': 13, 'Bipasha Basu': 14, 'Chitrangadha Singh': 15, 'Deepika Padukone': 16, 'Diana Penty': 17, 'Disha Patani': 18, 'Gul Panang': 19, 'Huma Qureshi': 20, "Ilean D'cruz": 21, 'Jacqueline Fernandez': 22, 'Janhvi Kapoor': 23, 'Kajal Agrawal': 24, 'Kajol': 25, 'Kalki Koechlin': 26, 'Kangana Ranaut': 27, 'Kareena Kapoor': 28, 'Katrina Kaif': 29, 'Kiara Advani': 30, 'Kirti Kulhari': 31, 'Kriti Kharbanda': 32, 'Kriti Sanon': 33, 'Kritika Kamra': 34, 'Lara Dutta': 35, 'Lauren Gottlieb': 36, 'Madhuri Dixit': 37, 'Mahira Khan': 38, 'Malavika Mohanan': 39, 'Mawra Hocane\xa0': 40, 'Mithila Palkar': 41, 'Mouni Roy': 42, 'Mrunal Thakur': 43, 'Nargis Fakhri': 44, 'Neha Dhupia': 45, 'Nimrat Kaur': 46, 'Nushrat Bharucha': 47, 'Padmapriya Janakiraman': 48, 'Pallavi Sharda': 49, 'Parineeti Chopra': 50, 'Pooja Hegde': 51, 'Radhika Apte': 52, 'Rakul Preet Kaur': 53, 'Rani Mukerji': 54, 'Rekha': 55, 'Richa Chadda': 56, 'Rishi Kapoor': 57, 'Saba Qamar': 58, 'Sanaya Malhotra': 59, 'Sapna Pabbi': 60, 'Sara Ali Khan': 61, 'Shraddha Kapoor': 62, 'Shriya Saran': 63, 'Shruti Hassan': 64, 'Sonakshi Sinha': 65, 'Sonam Kapoor': 66, 'Sridevi': 67, 'Swastika Mukherjee': 68, 'Taapsee Pannu': 69, 'Tara Sutaria': 70, 'Tena Desae': 71, 'Tisca Chopra': 72, 'Urvashi Rautela': 73, 'Vani Kapoor': 74, 'Vidya Balan': 75, 'Warina Hussain': 76, 'Yami Gautam': 77, 'Zaira Wasim': 78, 'Zareen Khan': 79, 'Zhu Zhu': 80}
            final_features.append(d[features[2]])
        elif i==3:
            d={'A': 0, 'U/A': 1}
            final_features.append(d[features[3]])
        elif i==4:
            d={'1.0': 0, '1.5': 1, '2.0': 2, '2.5': 3, '3.0': 4, '3.5': 5, '4.0': 6,'4.5': 7, '5.0': 8}
            final_features.append(d[str(features[4])])
        else:
            d={'N': 0, 'Y': 1}
            final_features.append(d[features[i]])
    
    final=[np.array(final_features)]
    classification=model_one.predict(final)
    #x=model_one.predict_proba(final)
    if classification==0:
        return render_template("mv-1.html", pred="Target Audience is Family.",ts="Releasing the movie during the Diwali Vacations")
        
    elif classification==1:
        return render_template("mv-1.html", pred="Target Audience is Kids.",ts="April-June& December")
        
    elif classification==2:
        return render_template("mv-1.html", pred="Target Audience is Middle-Aged.",ts="Bank Holidays")
        
    elif classification==3:
        return render_template("mv-1.html", pred="Target Audience is Middle Aged + Youngsters.",ts="Bank Holidays and Festive Season")
        
    elif classification==4:
        return render_template("mv-1.html", pred="Target Audience is Teens.",ts="College days")
        
    elif classification==5:
        return render_template("mv-1.html", pred="Target Audience is Youngsters.",ts="Late Evenings")
    
if __name__=="__main__":
    app.run()
        
    