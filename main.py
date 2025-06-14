from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime, date, timedelta

app = Flask(__name__)
app.secret_key = 'pet-carinho'
global LOGADO
LOGADO = 999
global HOJE
HOJE = date.today()
global AGORA
AGORA = datetime.now()

usuarios = [
    { 'tipo': 0,
      'codigo': 0,
      'nome': 'adm_vet',
      'email': 'adm@vet.com',
      'data_nascimento': '--/--/----',
      'endereco': 'N/A',
      'cep': 'N/A',
      'telefone': 'N/A',
      'senha': 'AuMiau'
    },
    {'tipo': 1,
      'codigo': 1,
      'nome': 'Maria',
      'email': 'maria@gmail.com',
      'data_nascimento': '2000-09-19',
      'endereco': 'N/A',
      'cep': 'N/A',
      'telefone': 'N/A',
      'senha': 'Maria@1'
    },
    {'tipo': 2,
      'codigo': 2,
      'nome': 'Gustavo',
      'email': 'gustavo@vet.com',
      'data_nascimento': '1999-03-06',
      'endereco': 'N/A',
      'cep': 'N/A',
      'telefone': 'N/A',
      'senha': 'Gustavo@1'
    },

    {'tipo': 1,
      'codigo': 3,
      'nome': 'Carlos',
      'email': 'carlos@gmail.com',
      'data_nascimento': '1985-12-05',
      'endereco': 'Rua das Flores, 123',
      'cep': '12345-678',
      'telefone': '(11) 91234-5678',
      'senha': 'Carlos@1'
    },
    {'tipo': 1,
      'codigo': 4,
      'nome': 'Ana',
      'email': 'ana@gmail.com',
      'data_nascimento': '1990-06-20',
      'endereco': 'Av. Brasil, 456',
      'cep': '23456-789',
      'telefone': '(21) 99876-5432',
      'senha': 'Ana@1'
    },

    {
        'tipo': 2,
        'codigo': 5,
        'nome': 'Mariana',
        'numero_registro': 'CRMV-12345',
        'email': 'mariana@vet.com',
        'telefone': '(31) 98765-4321',
        'senha': 'Mariana@1'
    },
    {
        'tipo': 2,
        'codigo': 6,
        'nome': 'João',
        'numero_registro': 'CRMV-67890',
        'email': 'joao@vet.com',
        'telefone': '(41) 91234-8765',
        'senha': 'Joao@1'
    }
]


animais = [
    { 'tutor': 1,
      'codigo': 0,
      'nome': 'Kiara',
      'data_nascimento': '2021-04-30',
      'especie': 'cachorro',
      'raca': 'SRD',
      'peso': 7.0,
      'sexo': 'F'
    },

    { 'tutor': 3,
      'codigo': 1,
      'nome': 'Rex',
      'data_nascimento': '2019-08-15',
      'especie': 'cachorro',
      'raca': 'Labrador',
      'peso': 30.5,
      'sexo': 'M'
    },
    { 'tutor': 3,
      'codigo': 2,
      'nome': 'Luna',
      'data_nascimento': '2020-12-01',
      'especie': 'gato',
      'raca': 'Siamês',
      'peso': 4.2,
      'sexo': 'F'
    },
    { 'tutor': 3,
      'codigo': 3,
      'nome': 'Bunny',
      'data_nascimento': '2022-05-10',
      'especie': 'coelho',
      'raca': 'Angorá',
      'peso': 2.3,
      'sexo': 'F'
    },
    { 'tutor': 3,
      'codigo': 4,
      'nome': 'Cali',
      'data_nascimento': '2023-01-25',
      'especie': 'calopsita',
      'raca': 'N/A',
      'peso': 0.1,
      'sexo': 'M'
    },

    { 'tutor': 4,
      'codigo': 5,
      'nome': 'Bolt',
      'data_nascimento': '2018-07-07',
      'especie': 'cachorro',
      'raca': 'Pastor Alemão',
      'peso': 35.0,
      'sexo': 'M'
    },
    { 'tutor': 4,
      'codigo': 6,
      'nome': 'Mia',
      'data_nascimento': '2022-02-20',
      'especie': 'gato',
      'raca': 'Maine Coon',
      'peso': 5.0,
      'sexo': 'F'
    },
    { 'tutor': 4,
      'codigo': 7,
      'nome': 'Fluffy',
      'data_nascimento': '2021-11-15',
      'especie': 'coelho',
      'raca': 'Mini Lop',
      'peso': 1.8,
      'sexo': 'M'
    },
    { 'tutor': 4,
      'codigo': 8,
      'nome': 'Piu Piu',
      'data_nascimento': '2023-03-10',
      'especie': 'calopsita',
      'raca': 'N/A',
      'peso': 0.1,
      'sexo': 'F'
    },
]
agendamentos = [{
        'ativo': True,
        'codigo': 0,
        'codigopet': 5,
        'nomepet': 'Bolt',
        'nometutor': 4,
        'telefone': '(21) 99876-5432',
        'codigovet': 2,
        'nomevet': 'Gustavo',
        'datahora': '2025-06-13T22:00',
        'sintomas': 'Tosse persistente',
        'datahora_obj': datetime(2025, 6, 13, 22, 0),
        'datahora_formatada': '13/06/2025 às 22:00',
        'data_somente': date(2025, 6, 13)
    },
    {
        'ativo': True,
        'codigo': 1,
        'codigopet': 0,
        'nomepet': 'Kiara',
        'nometutor': 1,
        'telefone': 'N/A',
        'codigovet': 2,
        'nomevet': 'Gustavo',
        'datahora': '2025-06-13T23:00',
        'sintomas': 'Febre e apatia',
        'remarcavel': True,
        'datahora_obj': datetime(2025, 6, 13, 23, 0),
        'datahora_formatada': '13/06/2025 às 09:00',
        'data_somente': date(2025, 6, 13),
    },
    {
        'ativo': True,
        'codigo': 2,
        'codigopet': 1,
        'nomepet': 'Rex',
        'nometutor': 3,
        'telefone': '(11) 91234-5678',
        'codigovet': 5,
        'nomevet': 'Mariana',
        'datahora': '2025-06-12T23:30',
        'sintomas': 'Coceira e queda de pelo',
        'remarcavel': True,
        'datahora_obj': datetime(2025, 6, 12, 23, 30),
        'datahora_formatada': '12/06/2025 às 14:30',
        'data_somente': date(2025, 6, 12),
    },
    {
        'ativo': True,
        'codigo': 3,
        'codigopet': 5,
        'nomepet': 'Bolt',
        'nometutor': 4,
        'telefone': '(21) 99876-5432',
        'codigovet': 6,
        'nomevet': 'João',
        'datahora': '2025-06-12T23:00',
        'sintomas': 'Dificuldade para andar',
        'remarcavel': True,
        'datahora_obj': datetime(2025, 6, 12, 23, 0),
        'datahora_formatada': '03/07/2025 às 11:00',
        'data_somente': date(2025, 6, 12),
    },
    {
        'ativo': True,
        'codigo': 4,
        'codigopet': 2,
        'nomepet': 'Luna',
        'nometutor': 3,
        'telefone': '(11) 91234-5678',
        'codigovet': 2,
        'nomevet': 'Gustavo',
        'datahora': '2025-06-13T15:15',
        'sintomas': 'Vômito frequente',
        'remarcavel': True,
        'datahora_obj': datetime(2025, 6, 13, 15, 15),
        'datahora_formatada': '13/06/2025 às 15:15',
        'data_somente': date(2025, 6, 13),
    },
    {
        'ativo': True,
        'codigo': 5,
        'codigopet': 7,
        'nomepet': 'Fluffy',
        'nometutor': 4,
        'telefone': '(21) 99876-5432',
        'codigovet': 5,
        'nomevet': 'Mariana',
        'datahora': '2025-07-05T08:45',
        'sintomas': 'Diarreia leve',
        'remarcavel': True,
        'datahora_obj': datetime(2025, 7, 5, 8, 45),
        'datahora_formatada': '05/07/2025 às 08:45',
        'data_somente': date(2025, 7, 5),
    },
    {
        'ativo': False,
        'codigo': 6,
        'codigopet': 0,
        'nomepet': 'Kiara',
        'nometutor': 1,
        'telefone': '(11) 91234-5678',
        'codigovet': 2,
        'nomevet': 'Gustavo',
        'datahora': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M'),
        'sintomas': 'Exemplo de agendamento passado',
        'remarcavel': False,
        'datahora_obj': datetime.now() - timedelta(days=1),
        'datahora_formatada': (datetime.now() - timedelta(days=1)).strftime('%d/%m/%Y às %H:%M'),
        'data_somente': (datetime.now() - timedelta(days=1)).date(),
        'prontuario': 'Não foi necessária medicação ou soro'
    }
]


@app.route('/')
def index():
    global LOGADO
    LOGADO = 999
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    global LOGADO
    try:
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            for usuario in usuarios:
                if usuario['email'] == email and usuario['senha'] == senha:
                    flash(f'Usuário {email} logado com sucesso!', 'sucesso')
                    if usuario['tipo'] == 0:
                        LOGADO = 0
                        return redirect('/dashboard')
                    elif usuario['tipo'] == 1:
                        LOGADO = 1
                        return redirect(url_for('pagina_usuario', codigo=usuario['codigo']))
                    elif usuario['tipo'] == 2:
                        LOGADO = 2
                        return redirect(url_for('pagina_veterinario', codigo=usuario['codigo']))
            else:
                flash('Nome e/ou senha incorretos. Tente novamente.', 'erro')
                return render_template('login.html')
        else:
            return render_template('login.html')
    except:
        flash(f'Um erro inesperado aconteceu', 'erro')
        return redirect('/login')

@app.route('/sair')
def sair():
    global LOGADO
    LOGADO = 999
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    try:
        global LOGADO
        LOGADO = 0
        tutores = []
        veterinarios = []
        animais_ativos = []
        agendamentos_futuros = []

        for a in agendamentos:
            if a['data_somente'] == HOJE:
                a['remarcavel'] = False
            if a['ativo'] == True and a['datahora_obj'] >= datetime.today() and 'prontuario' not in a:
                agendamentos_futuros.append(a)

        for usuario in usuarios:
            if usuario['tipo'] == 1 and usuario['nome'] != "":
                animais_do_usuario = []
                for animal in animais:
                    if animal['tutor'] == usuario['codigo'] and animal['nome'] != '':
                        animais_do_usuario.append(animal['nome'])
                tutor = {
                    'nome': usuario['nome'],
                    'codigo': usuario['codigo'],
                    'animais': animais_do_usuario
                }
                tutores.append(tutor)

            elif usuario['tipo'] == 2 and usuario['nome'] != "":
                veterinarios.append(usuario)

        for animal in animais:
            if animal['nome'] != '':
                data_obj = datetime.fromisoformat(animal['data_nascimento'])
                animal['data_nascimento_formatada'] = data_obj.strftime('%d/%m/%Y')
                animais_ativos.append(animal)

        return render_template('dashboard.html', tutores=tutores, veterinarios=veterinarios, animais=animais_ativos, LOGADO=LOGADO, codigo=0, agendamentos=agendamentos_futuros)
    except:
        flash(f'Ocorreu um erro ao carregar o dashboard do administrador', 'erro')
        return redirect('/')

@app.route('/pagina_veterinario/<int:codigo>')
def pagina_veterinario(codigo):
    try:
        global LOGADO
        LOGADO = 2
        usuario = ''
        for u in usuarios:
            if u['codigo'] == codigo:
                usuario = u
        if usuario and 'data_nascimento' in usuario and usuario['data_nascimento']:
            try:
                data_obj = datetime.fromisoformat(usuario['data_nascimento'])
                usuario['data_nascimento_formatada'] = data_obj.strftime('%d/%m/%Y')
            except ValueError:
                usuario['data_nascimento_formatada'] = usuario['data_nascimento']
        else:
            usuario['data_nascimento_formatada'] = "Não informado"
        agendamentos_vet = []
        animais_vet = []
        for a in agendamentos:
            if a['data_somente'] == HOJE:
                a['remarcavel'] = False
            if a['codigovet'] == usuario['codigo']:
                if a['ativo'] == True and a['datahora_obj'] >= datetime.today() and 'prontuario' not in a:
                    agendamentos_vet.append(a)
        for av in agendamentos_vet:
            for an in animais:
                if av['codigopet'] == an['codigo']:
                    if 'data_nascimento' in an and an['data_nascimento']:
                            data_animal = datetime.fromisoformat(an['data_nascimento'])
                            an['data_nascimento_formatada'] = data_animal.strftime('%d/%m/%Y')
                    else:
                        an['data_nascimento_formatada'] = "Não informado"
                    animais_vet.append(an)
        return render_template('pagina_veterinario.html', codigo=codigo, usuario=usuario, LOGADO=LOGADO, animais_vet=animais_vet, agendamentos_vet=agendamentos_vet)
    except Exception as e:
        flash(f'Ocorreu um erro inesperado {e}', 'erro')
        return redirect('/')

@app.route('/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    try:
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            data_nascimento = request.form.get('data-nascimento')
            endereco = request.form.get('endereco')
            cep = request.form.get('cep')
            telefone = request.form.get('telefone')
            senha = request.form.get('senha')
            for u in usuarios:
                if u['email'] == email:
                    flash('Esse e-mail já está cadastrado!', 'erro')
                    print(u)
                    return redirect('/cadastro_usuario')
            especiais = "!@#$%^&*()-_+=<>?/|\\{}[]"
            maiuscula = False
            minuscula = False
            especial = False
            numero = False
            for s in senha:
                if s.isupper():
                    maiuscula = True
                elif s.islower():
                    minuscula = True
                elif s.isdigit():
                    numero = True
                elif s in especiais:
                    especial = True
            if maiuscula == True and minuscula == True and numero == True and especial == True:
                codigo = len(usuarios)
                usuario = {
                    'tipo': 1,
                    'codigo': codigo,
                    'nome': nome,
                    'email': email,
                    'data_nascimento': data_nascimento,
                    'endereco': endereco,
                    'cep': cep,
                    'telefone': telefone,
                    'senha': senha
                }
                usuarios.append(usuario)
                flash(f'Usuário {nome} criado com sucesso!', 'sucesso')
                if LOGADO == 0:
                    return redirect('/dashboard')
                else:
                    return redirect('/login')
            else:
                flash('Utilize uma senha forte', 'erro')
                return render_template('cadastro_usuario.html', LOGADO=LOGADO)
        else:
            return render_template('cadastro_usuario.html', LOGADO=LOGADO)
    except:
        flash(f'Não foi possível criar esse usuário', 'erro')
        return render_template('cadastro_usuario.html', LOGADO=LOGADO)

@app.route('/edicao_usuario/<int:codigo>', methods=['GET', 'POST'])
def edicao_usuario(codigo):
    try:
        for u in usuarios:
            if u['codigo'] == codigo:
                usuario = u
                break
        if request.method == 'POST':
            novoemail = request.form["email"]
            senha = request.form.get('senha')
            especiais = "!@#$%^&*()-_+=<>?/|\\{}[]"
            maiuscula = False
            minuscula = False
            especial = False
            numero = False
            for s in senha:
                if s.isupper():
                    maiuscula = True
                elif s.islower():
                    minuscula = True
                elif s.isdigit():
                    numero = True
                elif s in especiais:
                    especial = True
            if maiuscula == True and minuscula == True and numero == True and especial == True:
                usuario['nome'] = request.form.get('nome')
                usuario['email'] = request.form.get('email')
                for u in usuarios:
                    if u["email"] == novoemail and u["codigo"] != usuario['codigo']:
                        flash('Este e-mail já está sendo usado')
                        break
                        return
                usuario['data_nascimento'] = request.form.get('data-nascimento')
                usuario['endereco'] = request.form.get('endereco')
                usuario['cep'] = request.form.get('cep')
                usuario['telefone'] = request.form.get('telefone')
                usuario['senha'] = request.form.get('senha')
                flash(f'Usuário {usuario["nome"]} editado com sucesso!', 'sucesso')
                if LOGADO == 0:
                    return redirect(url_for('dashboard'))
                elif LOGADO == 1:
                    return redirect(url_for('pagina_usuario', codigo=codigo))
                else:
                    return redirect('/')
            else:
                return render_template('edicao_usuario.html', usuario=usuario, LOGADO=LOGADO)
        return render_template('edicao_usuario.html', usuario=usuario, codigo=codigo, LOGADO=LOGADO)

    except:
        flash(f'Não foi possível editar esse usuário', 'erro')
        return render_template('edicao_usuario.html', usuario=usuario, LOGADO=LOGADO)

@app.route('/cadastro_animal/<int:codigo>', methods=['GET', 'POST'])
def cadastro_animal(codigo):
    try:
        if LOGADO == 1:
            usuario = usuarios[codigo]
        else:
            usuario = usuarios[0]
        tutores = []
        for u in usuarios:
            if u['tipo'] == 1:
                tutores.append(u)
        if request.method == 'POST':
            nome = request.form['nome']
            data_nascimento = request.form['data-nascimento']
            especie = request.form['especie']
            raca = request.form['raca']
            peso = float(request.form['peso'])
            sexo = request.form['sexo']
            codigoA = len(animais)
            if peso > 0:
                animal = {
                    'tutor': codigo,
                    'codigo': codigoA,
                    'nome': nome,
                    'data_nascimento': data_nascimento,
                    'especie': especie,
                    'raca': raca,
                    'peso': peso,
                    'sexo': sexo
                }
                animais.append(animal)
                flash(f'Pet {nome} cadastrado com sucesso!', 'sucesso')
                if LOGADO == 0:
                    return redirect(url_for('dashboard'))
                elif LOGADO == 1:
                    return redirect(url_for('pagina_usuario', codigo=codigo))
                else:
                    return redirect('/')
            else:
                flash(f'O peso deve ser maior que 0', 'erro')
                return render_template('cadastro_animal.html', codigo=codigo, LOGADO=LOGADO, tutores=tutores,
                                       usuario=usuario)
        else:
            return render_template('cadastro_animal.html', codigo=codigo, LOGADO=LOGADO, tutores=tutores, usuario=usuario)
    except:
        flash(f'Não foi possível cadastrar esse pet', 'erro')
        return redirect(url_for('pagina_usuario', codigo=codigo))

@app.route('/edicao_animal/<int:codigo>', methods=['POST', 'GET'])
def edicao_animal(codigo):
    try:
        animal = ''
        for a in animais:
            if a['codigo'] == codigo:
                animal = a
                break
        tutor = animal['tutor']
        print(tutor)
        if request.method == 'POST':
            peso = float(request.form.get('peso'))
            if peso > 0:
                animal['nome'] = request.form.get('nome')
                animal['data_nascimento'] = request.form.get('data_nascimento')
                animal['especie'] = request.form.get('especie')
                animal['raca'] = request.form.get('raca')
                animal['sexo'] = request.form.get('sexo')
                animal['peso'] = peso

                for a in agendamentos:
                    if a['codigopet'] == animal['codigo']:
                        a['nomepet'] = animal['nome']

                flash(f'Pet {animal["nome"]} editado com sucesso!', 'sucesso')
                if LOGADO == 0:
                    return redirect(url_for('dashboard'))
                elif LOGADO == 1:
                    return redirect(url_for('pagina_usuario', codigo=tutor))
                else:
                    return redirect('/')
            else:
                flash(f'O peso deve ser maior que 0', 'erro')
                return render_template('edicao_animal.html', animal=animal, codigo=codigo, LOGADO=LOGADO, tutor=tutor)
        else:
            return render_template('edicao_animal.html', animal=animal, codigo=codigo, LOGADO=LOGADO, tutor=tutor)
    except:
        flash(f'Ocorreu um erro inesperado', 'erro')
        return render_template('edicao_animal.html', animal=animal, codigo=codigo, LOGADO=LOGADO)

@app.route('/cadastro_veterinario', methods=['GET', 'POST'])
def cadastro_veterinario():
    try:
        if request.method == 'POST':
            nome = request.form['nome']
            numero_registro = request.form['numeroderegistro']
            telefone = request.form['telefone']
            email = request.form['email']
            for u in usuarios:
                if u['email'] == email:
                    flash('Esse e-mail já está cadastrado!', 'erro')
                    print(u)
                    return redirect('/cadastro_usuario')
            senha = request.form['senha']
            especiais = "!@#$%^&*()-_+=<>?/|\\{}[]"
            maiuscula = False
            minuscula = False
            especial = False
            numero = False
            for s in senha:
                if s.isupper():
                    maiuscula = True
                elif s.islower():
                    minuscula = True
                elif s.isdigit():
                    numero = True
                elif s in especiais:
                    especial = True
            if maiuscula == True and minuscula == True and numero == True and especial == True:
                codigo = len(usuarios)
                usuario = {
                    'tipo': 2,
                    'codigo': codigo,
                    'nome': nome,
                    'numero_registro': numero_registro,
                    'email': email,
                    'telefone': telefone,
                    'senha': senha
                }
                usuarios.append(usuario)
                flash(f'Veterinário {nome} cadastrado com sucesso!')
                return redirect('/dashboard')
            else:
                flash('Utilize uma senha forte', 'erro')
                return render_template('cadastro_veterinario.html', LOGADO=LOGADO)

        else:
            return render_template('cadastro_veterinario.html', LOGADO=LOGADO)
    except:
        flash(f'Não foi possível cadastrar esse veterinário')
        return redirect('/dashboard')

@app.route('/edicao_veterinario/<int:codigo>', methods=['GET', 'POST'])
def edicao_veterinario(codigo):
    try:
        for u in usuarios:
            if u['codigo'] == codigo:
                usuario = u
                break

        if request.method == 'POST':
            senha = request.form.get('senha')
            especiais = "!@#$%^&*()-_+=<>?/|\\{}[]"
            maiuscula = False
            minuscula = False
            especial = False
            numero = False
            for s in senha:
                if s.isupper():
                    maiuscula = True
                elif s.islower():
                    minuscula = True
                elif s.isdigit():
                    numero = True
                elif s in especiais:
                    especial = True
            if maiuscula == True and minuscula == True and numero == True and especial == True:
                email = request.form.get('email')
                for u in usuarios:
                    if u['email'] == email and u['codigo'] != usuario['codigo']:
                        flash('Esse e-mail já está cadastrado!', 'erro')
                        return render_template('edicao_veterinario.html', usuario=usuario, codigo=codigo, LOGADO=LOGADO)
                usuario['nome'] = request.form.get('nome')
                usuario['email'] = email
                usuario['numero_registro'] = request.form.get('numeroderegistro')
                usuario['telefone'] = request.form.get('telefone')
                usuario['senha'] = request.form.get('senha')
                for a in agendamentos:
                    if a['codigovet'] == usuario['codigo']:
                        a['nomevet'] = usuario['nome']

                flash(f'Veterinário {usuario["nome"]} editado com sucesso!', 'sucesso')
                if LOGADO == 0:
                    return redirect(url_for('dashboard'))
                elif LOGADO == 1:
                    return redirect(url_for('pagina_usuario', codigo=codigo))
                elif LOGADO == 2:
                    return redirect(url_for('pagina_veterinario', codigo=codigo))
                else:
                    return redirect('/')
            else:
                return render_template('edicao_veterinario.html', usuario=usuario, LOGADO=LOGADO)
        return render_template('edicao_veterinario.html', usuario=usuario, codigo=codigo, LOGADO=LOGADO)

    except:
        flash(f'Não foi possível editar esse veterinário', 'erro')
        return render_template('edicao_veterinario.html', usuario=usuario, LOGADO=LOGADO)

@app.route('/exclusao_veterinario/<int:codigo>', methods=['GET', 'POST'])
def exclusao_veterinario(codigo):
    try:
        usuario = ''
        for u in usuarios:
            if u['codigo'] == codigo:
                usuario = u
                break
        if request.method == 'POST':
            usuarios[codigo] = {
                'tipo': 2,
                'codigo': codigo,
                'nome': '',
                'numero_registro': '',
                'email': '',
                'telefone': '',
                'senha': ''
            }
            for a in agendamentos:
                if a['nomevet'] == usuario['nome']:
                    exclusao_agendamentos(a['codigo'])
            flash(f'Veterinário excluído com sucesso!', 'sucesso')
            return redirect(url_for('dashboard'))
        return render_template('exclusao_veterinario.html', codigo=codigo, usuario=usuario, LOGADO=LOGADO)
    except:
        flash(f'Ocorreu um erro inesperado', 'erro')
        return redirect('/dashboard')
@app.route('/pagina_usuario/<int:codigo>')
def pagina_usuario(codigo):
    try:
        global LOGADO
        LOGADO = 1
        for usuario in usuarios:
            if usuario['codigo'] == codigo:
                if 'data_nascimento' in usuario and usuario['data_nascimento']:
                    try:
                        data_obj = datetime.fromisoformat(usuario['data_nascimento'])
                        usuario['data_nascimento_formatada'] = data_obj.strftime('%d/%m/%Y')
                    except ValueError:
                        usuario['data_nascimento_formatada'] = usuario['data_nascimento']
                else:
                    usuario['data_nascimento_formatada'] = "Não informado"
                animais_do_usuario = []
                for animal in animais:
                    if animal['tutor'] == codigo:
                        if 'data_nascimento' in animal and animal['data_nascimento']:
                            try:
                                data_animal = datetime.fromisoformat(animal['data_nascimento'])
                                animal['data_nascimento_formatada'] = data_animal.strftime('%d/%m/%Y')
                            except ValueError:
                                animal['data_nascimento_formatada'] = animal['data_nascimento']
                        else:
                            animal['data_nascimento_formatada'] = "Não informado"
                        animais_do_usuario.append(animal)
                agendamentos_usuario = []
                for a in agendamentos:
                    if a['ativo'] == True and a['datahora_obj'] >= datetime.today():
                        if a['nometutor'] == usuario['codigo']:
                            if a['data_somente'] == HOJE:
                                a['remarcavel'] = False
                            agendamentos_usuario.append(a)
                return render_template('pagina_usuario.html', usuario=usuario, animais=animais_do_usuario, codigo=usuario['codigo'], LOGADO=LOGADO, agendamentos_usuario=agendamentos_usuario)
        flash("Usuário não encontrado", 'erro')
        return redirect('/')
    except:
        flash(f'Ocorreu um erro inesperado', 'erro')
        return redirect('/')

@app.route('/exclusao_usuario/<int:codigo>', methods=['GET', 'POST'])
def exclusao_usuario(codigo):
    try:
        usuario = ""
        for u in usuarios:
            if u['codigo'] == codigo:
                usuario = u
                animais_usuario = []
                break
        if request.method == 'POST':
            for a in animais:
                if a['tutor'] == usuario['codigo']:
                    exclusao_animal(a['codigo'])
            usuarios[codigo] = {
                'codigo': codigo,
                'tipo': "1",
                'nome': "",
                'email': "",
                'data_nascimento': "",
                'endereco': "",
                'cep': "",
                'telefone': "",
                'senha': "",
            }

            flash(f'Usuário excluído com sucesso!', 'sucesso')
            return redirect('/dashboard')
        return render_template('exclusao_usuario.html', usuario=usuario, animais=animais_usuario, codigo=usuario['codigo'], LOGADO=LOGADO)
    except:
        flash('Ocorreu um erro inesperado', 'erro')
        return redirect('/dashboard')

@app.route('/exclusao_animal/<int:codigo>', methods=['GET', 'POST'])
def exclusao_animal(codigo):
    try:
        animal = ''
        for a in animais:
            if a['codigo'] == codigo:
                animal = a
                break
        tutor = animal['tutor']
        if request.method == 'POST':
            for a in agendamentos:
                if a['codigopet'] == animal['codigo']:
                    exclusao_agendamentos(a['codigo'])
            animais[codigo] = {
                'tutor': tutor,
                'codigo': codigo,
                'nome': '',
                'data_nascimento': '',
                'especie': '',
                'raca': '',
                'peso': 0,
                'sexo': ''
            }

            flash(f'Pet excluído com sucesso!', 'sucesso')
            if LOGADO == 0:
                return redirect(url_for('dashboard'))
            elif LOGADO == 1:
                return redirect(url_for('pagina_usuario', codigo=tutor))
            else:
                return redirect('/')
        return render_template('exclusao_animal.html', codigo=codigo, LOGADO=LOGADO, animal=animal, tutor=tutor)
    except:
        flash(f'Ocorreu um erro inesperado', 'erro')
        if LOGADO == 0:
            return redirect(url_for('dashboard'))
        elif LOGADO == 1:
            return redirect(url_for('pagina_usuario', codigo=tutor))
        else:
            return redirect('/')
        
@app.route('/prontuario/<int:codigo_agendamento>', methods=['GET', 'POST'])
def prontuario(codigo_agendamento):
    try:
        print('entrnadoooooo')
        agendamento = ''
        veterinario = ''
        animal = ''
        recente = {'datahora': ''}
        for a in agendamentos:
            if a['codigo'] == codigo_agendamento:
                agendamento = a
                animal = animais[a['codigopet']]
        for ag in agendamentos:
            if ag['codigopet'] == animal['codigo'] and ag['datahora'] > recente['datahora'] and ag['datahora'] < agendamento['datahora']:
                recente = ag
        for v in usuarios:
            if v['codigo'] == agendamento['codigovet']:
                veterinario = v
        codigovet = int(veterinario['codigo'])
        data_obj = datetime.fromisoformat(animal['data_nascimento'])
        animal['data_nascimento_formatada'] = data_obj.strftime('%d/%m/%Y')
        if request.method == 'POST':
            receita = request.form.get('receita')
            if receita == "Soro" or receita == "Medicamento":
                return render_template('prontuario.html', codigo_agendamento=codigo_agendamento, agendamento=agendamento, animal=animal, tipo=receita, recente=recente, codigo=codigovet, LOGADO=LOGADO)
            else:
                agendamentos[codigo_agendamento]['prontuario'] = 'Não houve a prescrição de nenhum medicamento ou soro'
                agendamentos[codigo_agendamento]['ativo'] = False
                flash('Não houve a prescrição de nenhum medicamento ou soro', 'prontuario')
                if LOGADO == 2:
                    return redirect(url_for('pagina_veterinario', codigo=codigovet))
                else:
                    return redirect('/dashboard')
        else:
            return render_template('prontuario.html', codigo_agendamento=codigo_agendamento, agendamento=agendamento, animal=animal, recente=recente, codigo=codigovet, LOGADO=LOGADO)
    except:
        flash(f'Ocorreu um erro inesperado', 'erro')
        if LOGADO == 0:
            return redirect(url_for('dashboard'))
        elif LOGADO == 1:
            return redirect(url_for('pagina_usuario', codigo=codigovet))
        elif LOGADO == 2:
            return redirect(url_for('pagina_veterinario', codigo=codigovet))
        else:
            return redirect('/')

@app.route("/prontuario_soro/<int:codigo_agendamento>", methods=["GET", "POST"])
def prontuario_soro(codigo_agendamento):
    try:
        print('entrei')
        agendamento = ''
        veterinario = ''
        animal = ''
        recente = {'datahora': ''}
        print(recente)
        for a in agendamentos:
            if a['codigo'] == codigo_agendamento:
                agendamento = a
                animal = animais[a['codigopet']]
                print(animal)
        for a in agendamentos:
            if a['codigopet'] == animal['codigo']:
                if a['datahora'] > recente['datahora'] and a['datahora'] < agendamento['datahora']:
                    recente = a
                    print(recente)
        for v in usuarios:
            if v['codigo'] == agendamento['codigovet']:
                veterinario = v
                print(veterinario)
        codigovet = int(veterinario['codigo'])
        resultado_soro = ''
        print(codigovet)
        if request.method == "POST":
            valores_desidratacao = {
                'leve': 50,
                'moderada': 75,
                'grave': 100
            }

            desidratacao = request.form["desidratacao"]
            peso = float(request.form["peso_soro"])

            if peso <= 0:
                flash("Erro! Peso inválido", 'erro')
                return render_template("prontuario.html", animal=animal, agendamento=agendamento, codigo=codigovet, LOGADO=LOGADO, tipo="Soro")
            else:
                if desidratacao in valores_desidratacao:
                    resultado_soro = valores_desidratacao[desidratacao] * peso
                    agendamentos[codigo_agendamento]['prontuario'] = f'Soro: {resultado_soro}'
                    agendamentos[codigo_agendamento]['ativo'] = False

                    print(agendamentos)
                    flash(f"O volume para ser ministrado é de {resultado_soro} ml", 'prontuario')

                    if LOGADO == 0:
                        return redirect(url_for('dashboard'))
                    elif LOGADO == 1:
                        return redirect(url_for('pagina_usuario', codigo=codigovet))
                    elif LOGADO == 2:
                        return redirect(url_for('pagina_veterinario', codigo=codigovet))
                    else:
                        return redirect('/')
                else:
                    flash("Erro! Grau de desidratação inválido", 'erro')
                    return render_template("prontuario.html", animal=animal, agendamento=agendamento, codigo=codigovet, LOGADO=LOGADO, tipo="Soro")
            return render_template("prontuario.html", animal=animal, agendamento=agendamento, codigo=codigovet, LOGADO=LOGADO)
    except:
        flash(f'Ocorreu um erro inesperado', 'erro')
        if LOGADO == 0:
            return redirect(url_for('dashboard'))
        elif LOGADO == 1:
            return redirect(url_for('pagina_usuario', codigo=codigovet))
        elif LOGADO == 2:
            return redirect(url_for('pagina_veterinario', codigo=codigovet))
        else:
            return redirect('/')


@app.route("/prontuario_medicamento/<int:codigo_agendamento>", methods=["GET", "POST"])
def prontuario_medicamento(codigo_agendamento):
    try:
        if request.method == "POST":
            print('entrei')
            agendamento = ''
            veterinario = ''
            animal = ''
            recente = {'datahora': ''}
            for a in agendamentos:
                if a['codigo'] == codigo_agendamento:
                    agendamento = a
                    animal = animais[a['codigopet']]
                    print(animal)
            for a in agendamentos:
                if a['codigopet'] == animal['codigo']:
                    print(a['datahora'])
                    print(agendamento['datahora'])
                    print(recente['datahora'])
                    if a['datahora'] > recente['datahora'] and a['datahora'] < agendamento['datahora']:
                        recente = a
                        print(recente)
            for v in usuarios:
                if v['codigo'] == agendamento['codigovet']:
                    veterinario = v
                    print(veterinario)
            codigovet = veterinario['codigo']
            print(codigovet)
            resultado_dose = ''

            dose_recomendada = float(request.form["dose_recomendada"])
            peso = float(request.form["peso_medicamento"])

            if peso <= 0:
                flash("Erro! Peso inválido", 'erro')
                return render_template("prontuario.html", animal=animal, agendamento=agendamento, codigo=codigovet, LOGADO=LOGADO, tipo="Medicamento")
            elif dose_recomendada <= 0:
                flash("Erro! Dose inválida", 'erro')
                return render_template("prontuario.html", animal=animal, agendamento=agendamento, codigo=codigovet, LOGADO=LOGADO, tipo="Medicamento")
            else:
                resultado_dose = dose_recomendada * peso
                flash(f"A dose recomendada é {resultado_dose} mg", 'prontuario')
                agendamentos[codigo_agendamento]['prontuario'] = f'Medicamento: {resultado_dose}'
                agendamentos[codigo_agendamento]['ativo'] = False
                if LOGADO == 0:
                    return redirect(url_for('dashboard'))
                elif LOGADO == 2:
                    return redirect(url_for('pagina_veterinario', codigo=codigovet))
                else:
                    return redirect('/')
            return render_template("prontuario.html", animal=animal, agendamento=agendamento, LOGADO=LOGADO, codigo=codigovet)

    except:
        flash('Ocorreu um erro inesperado', 'erro')
        if LOGADO == 0:
            return redirect(url_for('dashboard'))
        elif LOGADO == 2:
            return redirect(url_for('pagina_veterinario', codigo=codigovet))
        else:
            return redirect('/')

@app.route('/agendamento/<int:codigo>', methods=["GET", "POST"])
def agendamento(codigo):
    try:
        if request.method == 'POST':
            codigopet = int(request.form["codigopet"])
            telefone = request.form["telefone"]
            codigovet = int(request.form["codigovet"])
            datahora = request.form["datahora"]
            sintomas = request.form["sintomas"]
            consulta = len(agendamentos)

            animal = animais[codigopet]
            nomeanimal = animal['nome']
            veterinario = usuarios[codigovet]
            tutor = animal['tutor']

            datahora_obj = datetime.fromisoformat(datahora)
            dia_da_semana = datahora_obj.weekday()
            hora_agendada = datahora_obj.hour
            datahora_obj = datetime.fromisoformat(datahora)
            datahora_formatada = datahora_obj.strftime("%d/%m/%Y às %H:%M")
            data_somente = datahora_obj.date()

            for a in agendamentos:
                if a['codigopet'] == codigopet and a['datahora_obj'] >= datetime.now() and a['ativo'] == True:
                    flash("Este pet já possui um agendamento", "erro")
                    return redirect(url_for('agendamento', codigo=codigo))
                elif a['datahora'] == datahora and a['codigovet'] == codigovet:
                    flash("Este horário não está disponível", "erro")
                    return redirect(url_for('agendamento', codigo=codigo))

            if datahora_obj < AGORA:
                flash("Não é possível agendar uma consulta no passado", "erro")
                return redirect(url_for('agendamento', codigo=codigo))

            if dia_da_semana == 6:
                flash("Desculpe, estamos fechados no domingo.", "erro")
                return redirect(url_for('agendamento', codigo=codigo))

            if dia_da_semana == 5:
                if hora_agendada < 8 or hora_agendada >= 14:
                    flash("O horário para sábado é das 08:00 às 14:00.", "erro")
                    return redirect(url_for('agendamento', codigo=codigo))
            else:
                if hora_agendada < 8 or hora_agendada >= 18:
                    flash("O horário para segunda a sexta é das 08:00 às 18:00.", "erro")
                    return redirect(url_for('agendamento', codigo=codigo))

            agendamento = {
                'codigo': int(consulta),
                'codigopet': codigopet,
                'nomepet': nomeanimal,
                'nometutor': int(tutor),
                'telefone': telefone,
                'codigovet': int(codigovet),
                'nomevet': veterinario['nome'],
                'datahora': datahora,
                'sintomas': sintomas,
                'remarcavel': True,
                'datahora_obj': datahora_obj,
                'datahora_formatada': datahora_formatada,
                'data_somente': data_somente,
                'ativo': True
            }
            agendamentos.append(agendamento)

            flash(f'Agendamento de {animal["nome"]} realizado com sucesso! Sua consulta será {datahora_formatada} com {veterinario["nome"]}.','sucesso')
            print(agendamentos)
            if LOGADO == 0:
                return redirect(url_for('dashboard'))
            elif LOGADO == 1:
                return redirect(url_for('pagina_usuario', codigo=codigo))
            else:
                return redirect('/')

        else:
            tutores = []
            veterinarios = []
            animais_usuario = []

            if LOGADO == 1:
                usuario = usuarios[codigo]
                for a in animais:
                    if a['tutor'] == usuario['codigo']:
                        animais_usuario.append(a)
            else:
                usuario = usuarios[0]

            for u in usuarios:
                if u['tipo'] == 1:
                    tutores.append(u)
                elif u['tipo'] == 2:
                    veterinarios.append(u)


            return render_template('agendamento.html', tutores=tutores, veterinarios=veterinarios, animais=animais, LOGADO=LOGADO, usuario=usuario, animais_usuario=animais_usuario)
    except:
            flash(f'Ocorreu um erro inesperado', 'erro')
            if LOGADO == 0:
                return redirect(url_for('dashboard'))
            elif LOGADO == 1:
                return redirect(url_for('pagina_usuario', codigo=codigo))
            else:
                return redirect('/')


@app.route('/reagendamento/<int:codigo_agendamento>', methods=['GET', 'POST'])
def reagendamento(codigo_agendamento):
    try:
        agendamento = {}
        for ag in agendamentos:
            if ag['codigo'] == int(codigo_agendamento):
                agendamento = ag
                break


        if not agendamento:
            flash("Agendamento não encontrado", "erro")
            if LOGADO == 0:
                return redirect(url_for('dashboard'))
            elif LOGADO == 1:
                return redirect(url_for('pagina_usuario', codigo=codigo_agendamento))
            else:
                return redirect('/')

        codigo = agendamento['nometutor']

        if request.method == 'POST':
            datahora = request.form["datahora"]
            codigopet = int(request.form["nomepet"])
            codigovet = int(request.form["codigovet"])
            veterinario = usuarios[codigovet]

            datahora_obj = datetime.fromisoformat(datahora)
            dia_da_semana = datahora_obj.weekday()
            hora_agendada = datahora_obj.hour
            datahora_obj = datetime.fromisoformat(datahora)
            datahora_formatada = datahora_obj.strftime("%d/%m/%Y às %H:%M")
            data_somente = datahora_obj.date()

            if datahora_obj < AGORA:
                flash("Não é possível agendar uma consulta no passado", "erro")
                return redirect(url_for('reagendamento', codigo_agendamento=codigo_agendamento))

            for a in agendamentos:
                if a['datahora'] == datahora and a['codigovet'] == codigovet and a['codigo'] != codigo_agendamento:
                    flash("Este horário não está disponível", "erro")
                    return redirect(url_for('reagendamento', codigo_agendamento=codigo_agendamento))

            if dia_da_semana == 6:
                flash("Desculpe, estamos fechados no domingo.", "erro")
                return redirect(url_for('reagendamento', codigo_agendamento=codigo_agendamento))

            if dia_da_semana == 5:
                if hora_agendada < 8 or hora_agendada >= 14:
                    flash("O horário para sábado é das 08:00 às 14:00.", "erro")
                    return redirect(url_for('reagendamento', codigo_agendamento=codigo_agendamento))
            else:
                if hora_agendada < 8 or hora_agendada >= 18:
                    flash("O horário para segunda a sexta é das 08:00 às 18:00.", "erro")
                    return redirect(url_for('reagendamento', codigo_agendamento=codigo_agendamento))

            agendamento['codigopet'] = int(request.form["nomepet"])
            agendamento['telefone'] = request.form["telefone"]
            agendamento['codigovet'] = int(request.form["codigovet"])
            agendamento['nomevet'] = veterinario['nome']
            agendamento['datahora'] = request.form["datahora"]
            agendamento['sintomas'] = request.form["sintomas"]
            agendamento['datahora_formatada'] = datahora_formatada
            agendamento['datahora_obj'] = datahora_obj
            agendamento['data_somente'] = data_somente

            flash(f'Agendamento do dia {agendamento['datahora_formatada']} editado com sucesso!', 'sucesso')
            if LOGADO == 0:
                return redirect(url_for('dashboard'))
            elif LOGADO == 1:
                return redirect(url_for('pagina_usuario', codigo=codigo))
            else:
                return redirect('/')

        else:
            tutores = []
            veterinarios = []
            animais_usuario = []

            if LOGADO == 1:
                usuario = usuarios[codigo]
                for a in animais:
                    if a['tutor'] == usuario['codigo']:
                        animais_usuario.append(a)
            else:
                usuario = usuarios[0]

            for u in usuarios:
                if u['tipo'] == 1:
                    tutores.append(u)
                elif u['tipo'] == 2:
                    veterinarios.append(u)
            return render_template('reagendamento.html', agendamento=agendamento, tutores=tutores,
                                   veterinarios=veterinarios, animais=animais, LOGADO=LOGADO, usuario=usuario,
                                   animais_usuario=animais_usuario)

    except:
        flash(f'Ocorreu um erro inesperado', 'erro')
        if LOGADO == 0:
            return redirect(url_for('dashboard'))
        elif LOGADO == 1:
            return redirect(url_for('pagina_usuario', codigo=codigo))
        else:
            return redirect('/')

@app.route('/exclusao_agendamentos/<int:codigo_agendamento>', methods=['GET', 'POST'])
def exclusao_agendamentos(codigo_agendamento):
    try:
        agendamento = ''
        for ag in agendamentos:
            if ag['codigo'] == codigo_agendamento:
                agendamento = ag
                break

        codigo = agendamento['nometutor']

        if request.method == 'POST':
            agendamentos[codigo_agendamento] = {
                'codigo': agendamento['codigo'],
                'codigopet': '',
                'nomepet': '',
                'nometutor': '',
                'telefone': '',
                'nomevet': '',
                'datahora': '',
                'sintomas': '',
                'remarcavel': False,
                'datahora_obj': '',
                'datahora_formatada': '',
                'data_somente': '',
                'ativo': False
            }
            print(agendamentos)

            flash(f'Agendamento excluído com sucesso!', 'sucesso')
            if LOGADO == 0:
                return redirect(url_for('dashboard'))
            elif LOGADO == 1:
                return redirect(url_for('pagina_usuario', codigo=codigo))
            else:
                return redirect('/')

            flash(f'Não foi possível excluir esse agendamento', 'erro')
            print('passei ak ')
            return render_template('exclusao_agendamentos.html', agendamento=agendamento, codigo=codigo, LOGADO=LOGADO)
        return render_template('exclusao_agendamentos.html', agendamento=agendamento, codigo=codigo, LOGADO=LOGADO)

    except:
        flash(f'Ocorreu um erro inesperado', 'erro')
        if LOGADO == 0:
            return redirect(url_for('dashboard'))
        elif LOGADO == 1:
            return redirect(url_for('pagina_usuario', codigo=codigo))
        else:
            return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)