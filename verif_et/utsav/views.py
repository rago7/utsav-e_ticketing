from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

# Create your views here.

def verify_user(pk):
    try:
        df = pd.read_excel('R:/Documents/projects/utsav e_ticketing/people.xlsx')
        filtered_rows = df[df['Identifier'] == pk]
        if not filtered_rows.empty:
            return filtered_rows.iloc[0]['Name']
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def sample(req, pk):
    verified = verify_user(pk)
    if verified:
        context = {'name':verified}
        return render(req, 'utsav/successful.html', context)
    else:
        return render(req, 'utsav/failure.html')