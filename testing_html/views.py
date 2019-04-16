from django.shortcuts import render


def basics(request):
    return render(request, 'basics.html', {})


def lists(request):
    return render(request, 'lists.html', {})


def div_spans(request):
    return render(request, 'div_spans.html', {})


def attributes(request):
    return render(request, 'attributes.html', {})


def level_one_assessment(request):
    return render(request, 'level_one_assessment.html', {})


def tables(request):
    return render(request, 'tables.html', {})


def tables_quiz(request):
    return render(request, 'tables_quiz.html', {})


def forms_basic(request):
    return render(request, 'forms_basics.html', {})


def forms_action_labels(request):
    return render(request, 'forms_actions_labels.html', {})


def forms_selections(request):
    return render(request, 'forms_selections.html', {})