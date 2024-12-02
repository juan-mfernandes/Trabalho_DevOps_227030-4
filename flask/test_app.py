import unittest
from app import app, db, Aluno

class TestAluno(unittest.TestCase):

    def setUp(self):
        # Configurar o ambiente de teste
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória para testes
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Limpar o banco de dados após cada teste
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_adicionar_aluno(self):
        # Dados do aluno para teste
        aluno_data = {
            'nome': 'Teste Aluno',
            'ra': '12345'
        }

        # Fazer a requisição POST para cadastrar o aluno
        response = self.app.post('/alunos', json=aluno_data)

        # Verificar se a resposta HTTP é 201 (Created)
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Aluno adicionado com sucesso!', response.data)

        # Verificar se o aluno foi adicionado no banco
        with app.app_context():
            aluno = Aluno.query.filter_by(ra='12345').first()
            self.assertIsNotNone(aluno)
            self.assertEqual(aluno.nome, 'Teste Aluno')

if __name__ == '__main__':
    unittest.main()
