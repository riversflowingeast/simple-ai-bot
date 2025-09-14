from flask import Flask, render_template, request
import os
from openai import OpenAI

client=OpenAI() # load OpenAI API client instance

app=Flask(__name__) # create Flask app, pass the import name

@app.route('/', methods=['GET','POST']) # decorator that tells Flask, when a user visits the home page, these are the acceptable methods and run the function below.
def home():
    response = ""
    if request.method=='POST':
        user_input=request.form["user_input"] # get the user's prompt entry
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=(
                {"role":"system","content":"You are a helpful assistant."},
                {"role":"user","content":user_input}

            )
        )
        response=completion.choices[0].message.content # by default, chat completions API model only returns one response (n=1)
    return render_template("index.html",response=response) #Send model output to the front-end

if __name__=="__main__":  #best practice to always include this in Flask scripts
    app.run(debug=True)
