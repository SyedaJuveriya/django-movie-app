from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

#Movies Data Here
movies = [
    {
        'id': 1,
        'title': 'Avengers: Endgame',
        'year': '2019',
        'description': 'The Avengers assemble once more in order to reverse Thanos\' actions and restore balance to the universe.',
        'poster': 'avengersendgame.jpg'
    },
    {
        'id': 2,
        'title': 'Inception',
        'year': '2010',
        'description': 'A thief who steals corporate secrets through dream-sharing is given the inverse task of planting an idea.',
        'poster': 'inception.jpg'
    },
    {
        'id': 3,
        'title': 'The Dark Knight',
        'year': '2008',
        'description': 'Batman sets out to dismantle the remaining criminal organizations that plague Gotham.',
        'poster': 'the-dark-knight.jpg'
    },
    {
        'id': 4,
        'title': 'Interstellar',
        'year': '2014',
        'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity’s survival.',
        'poster': 'Interstellar.jpg'
    },
    {
        'id': 5,
        'title': 'Titanic',
        'year': '1997',
        'description': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.',
        'poster': 'titanic.jpg'
    },
    {
        'id': 6,
        'title': 'The Matrix',
        'year': '1999',
        'description': 'A computer hacker learns about the true nature of his reality and his role in the war against its controllers.',
        'poster': 'matrix.jpg'
    },
    {
        'id': 7,
        'title': 'Gladiator',
        'year': '2000',
        'description': 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family.',
        'poster': 'gladiator.jpg'
    },
    {
        'id': 8,
        'title': 'Joker',
        'year': '2019',
        'description': 'In Gotham City, a mentally troubled comedian embarks on a downward spiral that leads to the creation of an iconic villain.',
        'poster': 'joker.jpg'
    },
    {
        'id': 9,
        'title': 'Forrest Gump',
        'year': '1994',
        'description': 'The story of a man with a low IQ who recounts the early years of his life and how he touched many lives.',
        'poster': 'forest.jpg'
    },
    {
        'id': 10,
        'title': 'Avatar',
        'year': '2009',
        'description': 'A paraplegic Marine is dispatched to the moon Pandora on a unique mission and becomes torn between following orders and protecting the world.',
        'poster': 'avatar.jpg'
    }
]

def home_view(request):
    return render(request, 'movies/home.html')

def movie_list_view(request):
    return render(request,'movies/movie_list.html',{'movies':movies})

def movie_detail_view(request,id):
    movie = None
    for m in movies:
        if m['id']== id:
            movie = m
            break
    
    return render(request,'movies/movie_details.html',{'movie':movie})

def movie_json_view(request):
    return JsonResponse({'movies':movies})
