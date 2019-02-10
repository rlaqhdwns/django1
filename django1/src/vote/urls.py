#하위 URLConf.
#app_name : 하위 URLConf 파일의 등록된 URL들의 그룹명
#urlpatterns : URL과 뷰함수를 리스트형태로 등록하는 변수
from django.urls import path
from .views import *

#from .views import index, detail, result, vote, qregister, qupdata, qdelete
app_name = 'vote'
#기본 주소 : 127.0.0.1:8000/vote/
urlpatterns = [
    #웹 클라이언트가 127.0.0.1:8000/vote/ 요청 시 index 뷰함수 호출
    #name : 해당 URL, 뷰함수 등록에 대해서 별칭을 지정
    path('',index, name='index'),
    #127.0.0.1:8000/vote/숫자/
    path('<int:q_id>/', detail, name='detail'),
    path('vote/', vote, name='vote'),
    path('result/<int:q_id>/', result, name='result'),
    path('qr/',qregister, name='qr' ),
    #127.0.0.1:8000/vote/qu/Question객체에 id값
    path('qu/<int:q_id>/',qupdata, name='qu'),
    path('qd/<int:q_id>/',qdelete, name='qd'),
    path('cr/', cregister, name='cr'),
    path('cu/<int:c_id>/', cupdata, name='cu'),
    path('cd/<int:c_id>/', cdelete, name='cd'),
    ] 