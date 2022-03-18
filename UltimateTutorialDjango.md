<h1>Ultimate Tutorial</h1></br>

<a>https://www.youtube.com/playlist?list=PLjv17QYEBJPpd6nI-MXpIa4qR7prKfPQz</a>
</br>
</br>

<h1>#1 Startando projeto e configuração para português (BR)</h1>
Em Settings:</br>
Mudar a LANGUAGE_CODE para 'pt-br'</br>
e TIME_ZONE para = 'America/Brasilia'
</br>
</br>
Criando as tabelas do Django:</br>
<i>py manage.py migrate</i> (criar tabelas para o banco de dados)</br>
<i>py manage.py runserver</i> (rodar o server) [ctrl + C pra parar de rodar o server]</br>
<i>py manage.py createsuperuser</i> (criar usuário para acessar o DashBoard do Django)</br>
Para entrar no DashBoard precisa colocar /admin no final da url</br>
</br>
Criando módulos:</br>
São aplicações q podemos reutilizar em outros projetos</br>
<i>py manage.py startapp nome</i></br>
</br>
</br>
<h1>#2 Criação de um app (módulo) e configuração de views e urls</h1>
Views:</br>
<i>from django.views.generic import TemplateView</i></br>
Aqui é onde teremos nossas funções ou classes,
ex:</br>
class IndexView(TemplateView):</br>
    template_name = 'pastaDentroDoTemplate/index.html'</br>
</br>
Lá em settings precisamos importar a biblioteca os </br>
import os</br>
e adicionar em DIRS:</br>
'DIRS': [os.path.join(BASE_DIR, 'templates')],</br>
Basicamente só pra buscar todos os templates e colocar na pasta de templates</br>
</br>
Templates:</br>
onde fica nossos arquivos .html</br>
sempre criar uma pasta template, e dentro dela, outra pasta com o mesmo nome do app</br>
</br>
Urls.py:</br>
Arquivo que vai guardar as urls de cada app, precisa criar</br>
from django.urls import path (importar o path)</br>
from .views import IndexView (importar as views)</br>
Nesse arquivo colocar:</br>
urlpatterns = [</br>
    path('endereço/', View.as_view(), name='nome da url'),</br>
]</br>
Incluir nas urls do projeto principal:</br>
Importar include</br>
path('endereço/', include('nome da app.urls')),</br>
</br>
E por último precisa ativar a app no INSTALLED_APPS:</br>
'nome.apps.NomeConfig',</br>
</br>
</br>
<h1>#3 Configurar arquivos estáticos (CSS, JS, imagens)</h1>
Criar pasta chamada static na raiz</br>
E dentro dela criar mais pastas para o q vc quiser colocar</br>
css, js, img</br>
Criar lá em settings.py um diretório para os arquivos do static</br>
STATICFILES_DIRS = [</br>
os.path.join(BASE_DIR, 'static')</br>
]</br>
E para pode carregar esses arquivos nos seus aquivos .html:</br>
{% load static %}</br>
link rel="stylesheet" href="{% static 'caminho do arquivo/nome do arquivo' %}"</br>
Pra por imagens, basta salvar na pasta img do static</br>
img src="{% static 'caminho do arquivo/nome do arquivo' %}" width='200' alt=""</br>
</br>
</br>
<h1>#4 Configurar e reutilizar templates com blocos</h1>
Criando um modelo.html onde conterá seu design modelo que estará em todas as páginas</br>
Usando {% block name %}{% endblock %}</br>
Assim vc n vai precisar colocar em todos os arquivos .html, só vai precisar herdar do modelo.html</br>
Basta colocar um {% extends 'pasta/modelo.html' %}</br>
E para mudar o conteúdo dos blocos basta mundar dentro deles</br>
</br>
</br>
<h1>#5 Criando links para as urls (baseado no "name" da url)</h1>
Mexe no href dos templates</br>
Basta colocar '{% url 'name' %}(o nome q agt define lá nos urlpatterns)</br>
</br>
</br>
<h1>#6 Arquitetura App View Template (MVT)</h1>
Resumo de como o django funciona</br>
</br>
</br>
<h1>#7 Introdução ao models.py para criação de classes e atributos</h1>
Todo Campo terá uma Atividade, e devemos dizer as propriedades de ambos, usando os Fields</br>
Sendo q cada Atividade vai ter uma ForeignKey para indicar o Campo</br></br>
E já consegue ver pelo admin as classes criadas mas tem q alterar o arquivo admin.py do app, para que apareça lá no /admin:</br>
from .models import Campo, Atividade</br>
admin.site.register(Campo)</br>
admin.site.register(Atividade)</br>
Mas ainda falta criar as tabelas no banco de dados, ai só dar um </br>
makemigrations e migrate no terminal</br></br></br>
<h1>#8 Criando um formulário para inserir registros (CreateView)</h1>
Nas views importar:</br>
from django.views.generic.edit import CreateView</br>
from.models import Campo, Atividade</br>
from django.urls import reverse_lazy</br>
e definir suas classes q serão criadas</br>
class CampoCreate(CreateView):</br>
    model = Campo(nome da Model)</br>
    fields = ['nome', 'descricao'](campos a serem preenchidos no formulário)</br>
    template_name = 'cadastro/form.html'(template que será usado)</br>
    success_url = reverse_lazy('index')(url a ser redirecionado quando dar enter)</br></br>
Nas urls.py:</br>
Importar as views criadas anteriormente:</br>
from .views import CampoCreate, AtividadeCreate</br>
e adicionar as respectivas urls:</br>
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),</br>
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),</br>
e por último colocar esse conjuntos de urls no urls.py central</br></br>
Criar templates:</br>
dentro do arquivo form.html:</br>
form action="", method="POST"</br>
    {% csrf_token %}</br>
    {{ form.as_p }}</br>
    button type="submit" class="btn btn-primary">Cadastrar/button</br>
/form</br></br></br>
<h1>#9 Atualizar registros (UpdateView)</h1>
Importar UpdateView nas views</br>
definir as classes da mesma forma q no CreateView</br></br>
Nas urls.py:</br>
importar suas novas views e definir os caminhos:</br>
from .views import CampoUpdate, AtividadeUpdate</br>
path('editar/campo/int:pk>', CampoUpdate.as_view(), name='editar-campo'),</br>
path('editar/atividade/int:pk>', AtividadeUpdate.as_view(), name='editar-atividade'),</br>
o int:pk é pra pegar o id exato da view q vc quer editar</br>
e pronto, já consegue editar suas models</br></br></br>
<h1>#10 Excluir registros (DeleteView) e mostrar os dados do objeto no template</h1>
Importar DeleteView nas views</br>
e criar as novas views, mas n precisa colocar os fields</br>
class CampoDelete(DeleteView):</br>
    model = Campo</br>
    template_name = 'cadastros/form-excluir.html'</br>
    success_url = reverse_lazy('index')</br></br>
agora na urls.py, importar suas novas views e definir os caminhos</br>
path('excluir/campo/int:pk>', CampoDelete.as_view(), name='excluir-campo'),</br>
</br>
agora criar o arquivo form-excluir.html:</br>
dentro do forms:</br>
Deseja excluir o registro: {{ object }}</br>
ele trata as models como 'object'</br>
e graças ao on_delete:'PROTECT', só se´ra possível excluir um campo, se n tiver nenhuma atividade nele</br></br></br>
<h1>#11 Listar registros/objetos com o ListView e laço de repetição (for) no template</h1>
Importar lá nas views:</br>
from django.views.generic.list import ListView</br>
e na criação das classe, só colocar o model e o template_name</br>
class CampoList(ListView):</br>
    model = Campo</br>
    template_name = 'cadastros/listas/campo.html'</br></br>
    class AtividadeList(ListView):</br>
    model = Atividade</br>
    template_name = 'cadastros/listas/atividade.html'</br></br>
mas aqui cada view terá seu próprio arquivo .html</br></br>
Nas urls.py, mesma coisa, importar as novas views e criar os caminhos:</br>
from .views import CampoList, AtividadeList</br>
path('listar/campo/', CampoList.as_view(), name='listar-campo'),</br>
path('listar/atividade/', AtividadeList.as_view(), name='listar-atividade'),</br></br>
No template de campo.html criar a visualização em colunas por uma tabela por meio de um 'for'</br>
</br></br>








