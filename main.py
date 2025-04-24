from dotenv import load_dotenv
import os

load_dotenv()

form_res_table_url = os.getenv('FORM_RES_TABLE_URL')

print(form_res_table_url)