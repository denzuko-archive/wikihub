from wikihub.wiki.models import Page
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

try:
  import markdown2
except ImportError:
  sys.stderr.write('Error: Markdown2 was not found please install')
  sys.exit(1)

def view_page(request, page_name):
  view="view.html"

  try:
    page = Page.objects.get(pk=page_name)
    objects = {
      "page_name":page_name,
      "Content":markdown2.markdown(page.content)
    }
    
  except Page.DoesNotExist:
    view = "create.html"
    objects = {"page_name":page_name}

  return render(view, objects)


def edit_page(request, page_name):
  try:
    page = Page.objects.get(pk=page_name)
    content = page.content

  except Page.DoesNotExist:
    content = ""

  objects = {
      "page_name":page_name,
      "Content":content
  }
  return render("edit.html", objects)

def save_page(request, page_name):
  content = request.POST["content"]

  try:
    page = Page.objects.get(pk=page_name)
    page.content = content

  except Page.DoesNotExist:
    page = Page(title=page_name, content=content)

  page.save()
  return HttpResponseRedirect("/wikihup/"+page_name+"/")

def render(view="", objects={}):
  return render_to_response(view, objects)
