from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from flask_login import LoginManager

app = Flask(__name__)
app.static_folder = 'static'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

with app.app_context():
    upgrade()

from app import routes, models

def seed(db):

    db.session.query(models.Quiz).delete()
    db.session.query(models.Question).delete()
    db.session.query(models.Answer).delete()

    instances = db.session.query(models.Quiz).all()
    
    if(len(instances) == 0):
        print("Seeding Database")
        #Add all questions/answers to database
        db.session.add(models.Quiz(quizname='The Blockchain'))
        db.session.add(models.Quiz(quizname='Non-Fungible Tokens'))
        db.session.add(models.Quiz(quizname='Mining'))
        db.session.add(models.Quiz(quizname='Cryptocurrencies'))
        db.session.add(models.Quiz(quizname='Uses'))
        db.session.commit()

        #For each quiz create the questions
        blockchainQuiz = models.Quiz.query.filter_by(quizname='The Blockchain').first().id
        nftQuiz = models.Quiz.query.filter_by(quizname='Non-Fungible Tokens').first().id
        miningQuiz = models.Quiz.query.filter_by(quizname='Mining').first().id
        cryptocurrenciesQuiz = models.Quiz.query.filter_by(quizname='Cryptocurrencies').first().id
        usesQuiz = models.Quiz.query.filter_by(quizname='Uses').first().id

        db.session.add(models.Question(questiontext='What is a blockchain?', quizId=blockchainQuiz))
        db.session.add(models.Question(questiontext='What gives miners incentive to validate transactions on the blockchain?', quizId=blockchainQuiz))
        db.session.add(models.Question(questiontext='What allows the blockchain to be tamper-proof?', quizId=blockchainQuiz))

        db.session.add(models.Question(questiontext='What does it mean when a token is non-fungible?', quizId=nftQuiz))
        db.session.add(models.Question(questiontext='What happens when someone buys an NFT?', quizId=nftQuiz))
        db.session.add(models.Question(questiontext='Out of the following choices, what can’t be considered an NFT?', quizId=nftQuiz))

        db.session.add(models.Question(questiontext='How do crypto miners get paid?', quizId=miningQuiz))
        db.session.add(models.Question(questiontext='What is crypto mining?', quizId=miningQuiz))
        db.session.add(models.Question(questiontext='What happens after a transaction is verified between the miners?', quizId=miningQuiz))

        db.session.add(models.Question(questiontext='What is cryptocurrency?', quizId=cryptocurrenciesQuiz))
        db.session.add(models.Question(questiontext='What can make handling cryptocurrencies risky?', quizId=cryptocurrenciesQuiz))
        db.session.add(models.Question(questiontext='What makes cryptocurrency convenient?', quizId=cryptocurrenciesQuiz))

        db.session.add(models.Question(questiontext='Which cryptocurrency allows for untraceable transactions?', quizId=usesQuiz))
        db.session.add(models.Question(questiontext='Which of these is not currently a use case for cryptocurrencies?', quizId=usesQuiz))
        db.session.add(models.Question(questiontext='What is a key advantage of using Bitcoin to transfer money rather than using a bank?', quizId=usesQuiz))

        db.session.commit()

        #For each question create the answers
        q1 = models.Question.query.filter_by(questiontext='What is a blockchain?').first().id
        db.session.add(models.Answer(answertext = 'A distributed ledger on a peer-to-peer network', questionId=q1, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'A brokerage for cryptocurrency', questionId=q1, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'A form of cryptocurrency', questionId=q1, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'A central financial institution for cryptocurrency', questionId=q1, correctAnswer=False))
        db.session.commit()

        q2 = models.Question.query.filter_by(questiontext='What gives miners incentive to validate transactions on the blockchain?').first().id
        db.session.add(models.Answer(answertext = 'Recognition and praise from community', questionId=q2, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Fees from blockchain creators', questionId=q2, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'A block reward', questionId=q2, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'Access to the blockchain', questionId=q2, correctAnswer=False))
        db.session.commit()

        q4 = models.Question.query.filter_by(questiontext='What allows the blockchain to be tamper-proof?').first().id
        db.session.add(models.Answer(answertext = 'Decentralization', questionId=q4, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Immutability', questionId=q4, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'The peer-to-peer network of computers', questionId=q4, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Regulation', questionId=q4, correctAnswer=False))
        db.session.commit()

        #####

        q5 = models.Question.query.filter_by(questiontext='What does it mean when a token is non-fungible?').first().id
        db.session.add(models.Answer(answertext = 'It cannot be easily replicated or copied for something of similar value', questionId=q5, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'It is unique and can’t easily be substituted with something of similar value', questionId=q5, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'It is something that can be easily replicated but won’t have the same value as the original', questionId=q5, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'It i6 a token that can be a piece of art, like a video, or a picture, or a game', questionId=q5, correctAnswer=False))
        db.session.commit()

        q6 = models.Question.query.filter_by(questiontext='What happens when someone buys an NFT?').first().id
        db.session.add(models.Answer(answertext = 'They only claim the rights to attend an auction to get ownership of it', questionId=q6, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'They claim a copy of that NFT', questionId=q6, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'They become authenticated to view and copy the NFT only', questionId=q6, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'They claim ownership on that NFT', questionId=q6, correctAnswer=True))
        db.session.commit()

        q7 = models.Question.query.filter_by(questiontext='Out of the following choices, what can’t be considered an NFT?').first().id
        db.session.add(models.Answer(answertext = 'A diamond', questionId=q7, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Sports atheletes', questionId=q7, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Gold', questionId=q7, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'A tweet', questionId=q7, correctAnswer=True))
        db.session.commit()

        ####
        q8 = models.Question.query.filter_by(questiontext='How do crypto miners get paid?').first().id
        db.session.add(models.Answer(answertext = 'Cryptocurrency', questionId=q8, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'Money', questionId=q8, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Travel', questionId=q8, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Gold', questionId=q8, correctAnswer=False))
        db.session.commit()

        q9 = models.Question.query.filter_by(questiontext='What is crypto mining?').first().id
        db.session.add(models.Answer(answertext = 'Digging crypto from the ground', questionId=q9, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Maintenance and development of the blockchain ledger by solving mathematical equations', questionId=q9, correctAnswer=True))
        db.session.commit()


        q10 = models.Question.query.filter_by(questiontext='What happens after a transaction is verified between the miners?').first().id
        db.session.add(models.Answer(answertext = 'Get added to the memory pool which is then added to the Blockchain', questionId=q10, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'The money goes to the bank for verification', questionId=q10, correctAnswer=False))
        db.session.commit()


        ####
        q11 = models.Question.query.filter_by(questiontext='What is cryptocurrency?').first().id
        db.session.add(models.Answer(answertext = 'Digital currency created from code that goes through multiple complicated and slow processes to make a transaction', questionId=q11, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Currency people on the internet rely on for a convenient and easy way to make money', questionId=q11, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Digital currency that goes through a company before sending it to the intended receiver', questionId=q11, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Digital currency created from code that relies on cryptographic methods for transactions', questionId=q11, correctAnswer=True))
        db.session.commit()

        q12 = models.Question.query.filter_by(questiontext='What can make handling cryptocurrencies risky?').first().id
        db.session.add(models.Answer(answertext = 'It is not guaranteed that the transactions will be successful or safe', questionId=q12, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'People are anonymous when making transactions', questionId=q12, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'The cryptography used for transactions now is not reliable or safe enough to use', questionId=q12, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Transactions are anonymous', questionId=q12, correctAnswer=True))
        db.session.commit()

        q13 = models.Question.query.filter_by(questiontext='What makes cryptocurrency convenient?').first().id
        db.session.add(models.Answer(answertext = 'The money goes directly to the receiver, making a middleman handle the transfer unnecessary', questionId=q13, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'Authentication is always required from users before making a transaction', questionId=q13, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'It is guaranteed that transactions will successfully be received to the intended receiver', questionId=q13, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Nothing...there’s nothing convenient about it. It is risky, dodgy, and unpredictable', questionId=q13, correctAnswer=False))
        db.session.commit()

        ####

        q14 = models.Question.query.filter_by(questiontext='Which cryptocurrency allows for untraceable transactions?').first().id
        db.session.add(models.Answer(answertext = 'Bitcoin', questionId=q14, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Ethereum', questionId=q14, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'XMR', questionId=q14, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'Litecoin', questionId=q14, correctAnswer=False))
        db.session.commit()

        q15 = models.Question.query.filter_by(questiontext='Which of these is not currently a use case for cryptocurrencies?').first().id
        db.session.add(models.Answer(answertext = 'Investment', questionId=q15, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Fundraising', questionId=q15, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Transferring money', questionId=q15, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Operating machinery', questionId=q15, correctAnswer=True))
        db.session.commit()

        q16 = models.Question.query.filter_by(questiontext='What is a key advantage of using Bitcoin to transfer money rather than using a bank?').first().id
        db.session.add(models.Answer(answertext = 'Money can be sent at any time', questionId=q16, correctAnswer=True))
        db.session.add(models.Answer(answertext = 'Bitcoin can be insured', questionId=q16, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Bitcoin allows for simple transaction refunds', questionId=q16, correctAnswer=False))
        db.session.add(models.Answer(answertext = 'Bitcoin transactions are verified by government system', questionId=q16, correctAnswer=False))
        db.session.commit()

        print('#####DEBUG PRINT######')
        quizzes = db.session.query(models.Quiz).all()
        for quiz in quizzes:
            print('######')
            print(quiz.quizname)
            print('#####')
            questions = quiz.questions
            for question in questions:
                print('##')
                print(question.questiontext)
                print('##')
                answers = question.answers
                for answer in answers:
                    if answer.correctAnswer:
                        print(f'#{answer.answertext}#')
                    else: print(answer.answertext)




        



        








        

        #Fetch with quizname just to be safe 

seed(db)
