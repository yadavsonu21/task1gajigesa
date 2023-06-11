from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

# Create your views here.

# declaring base context dictionary named messages
messages = [
    {"role": "system", "content": "You are a helpful AI chatbot you need to help users in best possible manner."},
]


# function to update message prompt --- > to get context of chat from past convo in a session
# role -- system , user, assistant
def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


# method to get response from chatbot in which prompt is input + previous chat context
# here api key can be set into env varibales  replace it with your api key in this code
def get_response(prompt):
    openai.api_key = "YOUR_API_KEY"
    """replace with api key"""
    # here token limit is set upto 100 which can be modified as per need
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=prompt,
        max_tokens=100
    )
    if response.choices[0].message is not None:
        return response.choices[0].message
    else:
        return 'None'


#     this can be commmented out as of now it is for smooth working

@csrf_exempt
def home(request):
    """ Getting list of prompt """
    global messages
    if request.method == 'POST':
        #         getting user input
        user_input = request.POST['input']
        messages = update_chat(messages, "user", user_input)
        response = get_response(messages)
        # print(response)
        return JsonResponse({"response": response})
    return render(request, 'home.html')


def refresh(request):
    # to clear chat history by clearing list messages
    global messages
    messages = [
        {"role": "system", "content": "You are a helpful AI chatbot you need to help users in best possible manner."},
    ]
    return redirect(home)
