from django.urls import path, include
from django.contrib import admin
from . import views
from theme.views import index


urlpatterns = [
    path("index/",index,name="index"),
    path("viewTeam/", views.viewTeam, name="viewTeam"),
    path("matches/", views.matches, name="matches"),
    path("updateFutsalMatch/", views.updateFutsalMatch, name="updateFutsalMatch"),
    path("teamDetails/", views.teamDetails, name="teamDetails"),path("futsal", views.futsal, name="futsal"),
    path("futsalMatch/", views.futsalMatch, name="futsalMatch"),
    path('addTeam/', views.addTeam, name='addTeam'),



    # # api paths
    path('api/SearchByFutsalField/',views.SearchByFutsalField,name='SearchByFutsalField'),

    # path("api/deleteExpense/", views.deleteExpense, name="deleteExpense"),
    # path("api/searchByExpenseDate/", views.searchByExpenseDate, name="searchByExpenseDate"),
    # path("api/searchByExpenseHeadOfAccount/", views.searchByExpenseHeadOfAccount, name="searchByExpenseHeadOfAccount"),
    # path("api/searchByExpenseData/", views.searchByExpenseData, name="searchByExpenseData"),
    
]