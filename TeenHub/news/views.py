from django.shortcuts import render,redirect
from news.models import News

# Create your views here.
def show_news(request):
	if 'id' in request.session:
		news = News.objects.get(user_id=request.session['id'])
		print(news)
	else:
		print("inside else part")
		news = News(buzzfeed=1,daily_mail=1,entertainment_weekly=1,ign=1,mashable=1,mtv_news=1,polygon=1,the_lad_bible=1,ars_technica=1,crypto_coins_news=1,hacker_news=1,recode=1,techcrunch=1,techradar=1,the_next_web=1,the_verge=1,wired=1)
	return render(request, 'news/session_news.html', {'news' : news})

def save_all_news_list(request):
	if request.POST:
		print("inside save_news_list")
		#print(request.session['id'])
		allNewsList=News.objects.get(user_id=request.session['id'])
		if 'buzzfeed' not in request.POST:
			allNewsList.buzzfeed=0
		else:
			allNewsList.buzzfeed=request.POST['buzzfeed']
			print('buzzfeed')

		if 'daily_mail' not in request.POST:
			allNewsList.daily_mail=0
		else:
			allNewsList.daily_mail=request.POST['daily_mail']
			print('daily_mail')

		if 'entertainment_weekly' not in request.POST:
			allNewsList.entertainment_weekly=0
		else:
			allNewsList.entertainment_weekly=request.POST['entertainment_weekly']
			print('entertainment_weekly')

		if 'ign' not in request.POST:
			allNewsList.ign=0
		else:
			allNewsList.ign=request.POST['ign']
			print('ign')

		if 'mashable' not in request.POST:
			allNewsList.mashable=0
		else:
			allNewsList.mashable=request.POST['mashable']
			print('mashable')

		if 'mtv_news' not in request.POST:
			allNewsList.mtv_news=0
		else:
			allNewsList.mtv_news=request.POST['mtv_news']
			print('mtv_news')

		if 'polygon' not in request.POST:
			allNewsList.polygon=0
		else:
			allNewsList.polygon=request.POST['polygon']
			print('polygon')

		if 'the_lad_bible' not in request.POST:
			allNewsList.the_lad_bible=0
		else:
			allNewsList.the_lad_bible=request.POST['the_lad_bible']
			print('the_lad_bible')

		if 'ars_technica' not in request.POST:
			allNewsList.ars_technica=0
		else:
			allNewsList.ars_technica=request.POST['ars_technica']
			print('ars_technica')

		if 'crypto_coins_news' not in request.POST:
			allNewsList.crypto_coins_news=0
		else:
			allNewsList.crypto_coins_news=request.POST['crypto_coins_news']
			print('crypto_coins_news')

		if 'hacker_news' not in request.POST:
			allNewsList.hacker_news=0
		else:
			allNewsList.hacker_news=request.POST['hacker_news']
			print('hacker_news')

		if 'recode' not in request.POST:
			allNewsList.recode=0
		else:
			allNewsList.recode=request.POST['recode']
			print('recode')

		if 'techcrunch' not in request.POST:
			allNewsList.techcrunch=0
		else:
			allNewsList.techcrunch=request.POST['techcrunch']
			print('techcrunch')

		if 'techradar' not in request.POST:
			allNewsList.techradar=0
		else:
			allNewsList.techradar=request.POST['techradar']
			print('techradar')

		if 'the_next_web' not in request.POST:
			allNewsList.the_next_web=0
		else:
			allNewsList.the_next_web=request.POST['the_next_web']
			print('the_next_web')

		if 'the_verge' not in request.POST:
			allNewsList.the_verge=0
		else:
			allNewsList.the_verge=request.POST['the_verge']
			print('the_verge')

		if 'wired' not in request.POST:
			allNewsList.wired=0
		else:
			allNewsList.wired=request.POST['wired']
			print('wired')


		allNewsList.save()


		return redirect('/news')

def save_entertain_news_list(request):
	if request.POST:
		print("inside entertain")
		#print(request.session['id'])
		allNewsList=News.objects.get(user_id=request.session['id'])
		if 'buzzfeed' not in request.POST:
			allNewsList.buzzfeed=0
			print("qwerty11")
		else:
			allNewsList.buzzfeed=request.POST['buzzfeed']
			print('buzzfeed')

		if 'daily_mail' not in request.POST:
			allNewsList.daily_mail=0
		else:
			allNewsList.daily_mail=request.POST['daily_mail']
			print('daily_mail')

		if 'entertainment_weekly' not in request.POST:
			allNewsList.entertainment_weekly=0
		else:
			allNewsList.entertainment_weekly=request.POST['entertainment_weekly']
			print('entertainment_weekly')

		if 'ign' not in request.POST:
			allNewsList.ign=0
		else:
			allNewsList.ign=request.POST['ign']
			print('ign')

		if 'mashable' not in request.POST:
			allNewsList.mashable=0
		else:
			allNewsList.mashable=request.POST['mashable']
			print('mashable')

		if 'mtv_news' not in request.POST:
			allNewsList.mtv_news=0
		else:
			allNewsList.mtv_news=request.POST['mtv_news']
			print('mtv_news')

		if 'polygon' not in request.POST:
			allNewsList.polygon=0
		else:
			allNewsList.polygon=request.POST['polygon']
			print('polygon')

		if 'the_lad_bible' not in request.POST:
			allNewsList.the_lad_bible=0
		else:
			allNewsList.the_lad_bible=request.POST['the_lad_bible']
			print('the_lad_bible')

		allNewsList.save()

		return redirect('/news')

def save_tech_news_list(request):
	if request.POST:
		print("inside tech")
		#print(request.session['id'])
		allNewsList=News.objects.get(user_id=request.session['id'])
		if 'ars_technica' not in request.POST:
			allNewsList.ars_technica=0
		else:
			allNewsList.ars_technica=request.POST['ars_technica']
			print('ars_technica')

		if 'crypto_coins_news' not in request.POST:
			allNewsList.crypto_coins_news=0
		else:
			allNewsList.crypto_coins_news=request.POST['crypto_coins_news']
			print('crypto_coins_news')

		if 'hacker_news' not in request.POST:
			allNewsList.hacker_news=0
		else:
			allNewsList.hacker_news=request.POST['hacker_news']
			print('hacker_news')

		if 'recode' not in request.POST:
			allNewsList.recode=0
		else:
			allNewsList.recode=request.POST['recode']
			print('recode')

		if 'techcrunch' not in request.POST:
			allNewsList.techcrunch=0
		else:
			allNewsList.techcrunch=request.POST['techcrunch']
			print('techcrunch')

		if 'techradar' not in request.POST:
			allNewsList.techradar=0
		else:
			allNewsList.techradar=request.POST['techradar']
			print('techradar')

		if 'the_next_web' not in request.POST:
			allNewsList.the_next_web=0
		else:
			allNewsList.the_next_web=request.POST['the_next_web']
			print('the_next_web')

		if 'the_verge' not in request.POST:
			allNewsList.the_verge=0
		else:
			allNewsList.the_verge=request.POST['the_verge']
			print('the_verge')

		if 'wired' not in request.POST:
			allNewsList.wired=0
		else:
			allNewsList.wired=request.POST['wired']
			print('wired')


		allNewsList.save()
		return redirect('/news')
