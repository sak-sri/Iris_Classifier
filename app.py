from flask import Flask,render_template,request
import numpy as np
import pickle
from forms import SubmitData
app=Flask(__name__)
app.config['SECRET_KEY']="keep_it_secure"

def fetch_value(input_list):
    input_arr=np.array(input_list).reshape(1,4)
    loaded_model=pickle.load(open("model.pkl","rb"))
    result=loaded_model.predict(input_arr)
    return result[0]

@app.route("/",methods=['GET','POST'])
def result():
        form=SubmitData()
        if(form.validate_on_submit()):
            test_x=[form.sep_len.data,form.sep_width.data,form.pet_len.data,form.pet_width.data]
            ans=fetch_value(test_x)  
            if(ans==1):
                ans='Iris-setosa'
            elif(ans==2):
                ans='Iris-versicolor'
            else:
                ans='Iris-virginica'
            return render_template("submit_form.html",form=form,ans=ans)
        return render_template("submit_form.html",form=form)

if __name__=='__main__':
    app.run(threaded=True,port=5000)
