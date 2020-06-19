from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Task, mSequencia, Proteina
from .forms import TaskForm,SeqForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from Bio.Seq import Seq
import requests
import os

def tasksList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})


def tasksIndex(request):
    #return HttpResponse('index.html')
    return render(request, 'tasks/index.html')

def taskView(request, id):
    tasks = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'tasks': tasks})

def helloWorld(request):
    return HttpResponse('Hello World')

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=(task))

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

            
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request,'Tarefa deletada com sucesso.')
    
    return redirect('/')

def yourName(request, name):
    return render(request, 'tasks/yourname.html' ,{'name':name})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

def teste(request):
    #os.system("echo teste py")

    #Criando Lista de Sequencias vazia
    sequencias = []
    #DNA
    my_seq = Seq("AGTACACTGGT")
    #Transcrevendo o DNA para RNA
    seq_rna = my_seq.transcribe()
    #Adicionando a um dicionario
    dic_sequencias = {'DNA': my_seq, 'RNAm': seq_rna}
    print(my_seq)

    #Adicionando o dicionario a lista
    sequencias.append(dic_sequencias)
    
    return render(request, 'tasks/teste.html',{'sequencias': sequencias})
    
    # for k,v in tel.items():
    # print(k, " - ", v)


    # dados = []

    # resultado = []

    # dados.append(2)
    # dados.append(5)
    # dados.append(10)

    # resultado.append('teste1')
    # resultado.append('teste2')
    # resultado.append('teste3')



    # objTarefa = Task.objects.all().order_by('-created_at')
    
    # os.system('cd arquivo')
    # os.system('dir')
    # os.system('mkdir PastaTeste')


    # return render(request, 'tasks/teste.html',{'meusDados': dados, 'meusResultados': resultado, 'objTarefas': objTarefa})



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'tasks/upload.html', context)

def seq_list(request):
    sequencias = mSequencia.objects.all()
    return render(request, 'tasks/rna_list.html', {'sequencia': sequencias})

def upload_seq(request):
    #Criando lógica para receber dados

    if request.method == 'POST':
       #Criando variavel para receber os dados enviados por Formulário
        form = SeqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SeqForm()
    return render(request, 'tasks/upload_seq.html', {'form': form})


def testeCMD(request):
    #os.system('dir')
    #getModelo()
    proteinas = Proteina.objects.all().order_by('id')
    return render(request, 'tasks/testecmd.html',{'proteinas': proteinas})

def infoProteina(request, id):
    proteinas = get_object_or_404(Proteina, pk=id)
    return render(request, 'tasks/proteina.html', {'proteinas': proteinas})


def getModelo(request, id):
    qntmodelo = 2
    proteinas = get_object_or_404(Proteina, pk=id)
    #Dados da Sequência estão armazenados na proteinas.sequencia
    os.system('pyMOL sequencias/fasta/bgl.B99990001.pdb')
    return render(request, 'tasks/proteina.html', {'proteinas': proteinas})
    

# A Partir daqui serão criados os testes para a modelagem da Proteina
# Ao todo são x Fases identificadas:
