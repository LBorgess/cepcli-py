# CEP - Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Aplicação CLI desenvolvida em Python que realiza o consumo o *endpoint* de CEP da Brasil API. 

### Instalação

Realize o clone desse repositório

```bash
git clone
```

Acesse o diretório clonado e execute o comando abaixo para criar o ambiente virtual do Python.

```bash
python -m venv venv
```

Ative o ambiente virtual Python utilizando um dos  comandos abaixo.

<details>
<summary>Windows</summary>

O arquivo `.bat` é executado no CMD enquanto do `.ps1` no Windows Powershell

```bash
venv\Scripts\activate.bat
```

```bash
venv\Scripts\Activate.ps1
```

</details>

<details>
<summary>Linux</summary>

O comando abaixo também pode ser executado no Git Bash ( Windows ), trocando o `/bin/` por `/Scripts/`

```bash
source venv/bin/activate
```

</details>

Por fim, utilize o comando seguinte comando para realizar a instalação das dependências do projeto. 

```bash
pip install -r requirements.txt
```

### Execução

```bash
python main.py <cep>
```

### Requisitos

Necessário ter instalado o Python 3 e as dependências do arquivo `requirements.txt`
