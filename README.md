# 📊 Pipeline de Dados IoT

## 📌 Sobre o Projeto

Este projeto implementa um pipeline de dados para processamento de informações de dispositivos IoT. O objetivo é coletar dados de temperatura a partir de arquivos CSV, realizar transformações, armazenar em um banco de dados PostgreSQL e disponibilizar visualizações através de um dashboard interativo.

O pipeline segue as etapas fundamentais de engenharia de dados:

- Ingestão de dados
- Transformação
- Armazenamento
- Análise (via SQL)
- Visualização (dashboard)

---

## 🧠 Tecnologias Utilizadas

- Python  
- Pandas  
- SQLAlchemy  
- PostgreSQL  
- Docker  
- Streamlit  
- python-dotenv  

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd DAIOTBDIA
2. Criar e ativar ambiente virtual
python -m venv .venv
.venv\Scripts\activate
3. Instalar dependências
pip install pandas sqlalchemy psycopg2-binary python-dotenv streamlit
4. Configurar variáveis de ambiente

Crie um arquivo .env:

DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres

5. Subir o banco com Docker
docker-compose up -d

6. Executar o pipeline
python -m scripts.run_pipeline

7. Criar as views no banco
docker exec -it postgres-iot psql -U postgres
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT "room_id/id", AVG(temp) AS avg_temp
FROM temperature_readings
GROUP BY "room_id/id";

CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora,
COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora;

CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT 
DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS data,
MAX(temp) AS temp_max,
MIN(temp) AS temp_min
FROM temperature_readings
GROUP BY data;

8. Executar o dashboard

⚠️ Importante: Execute sempre a partir da raiz do projeto.

python -m streamlit run app/dashboard/dashboard.py
⚠️ Problema Comum
❌ Erro:
ModuleNotFoundError: No module named 'app'
✅ Solução:

Execute o Streamlit usando o modo módulo:

python -m streamlit run app/dashboard/dashboard.py

Isso garante que o Python reconheça corretamente a estrutura do projeto.