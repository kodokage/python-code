import pygame.mixer
sounds = pygame.mixer
sounds.init()

questions_number = 0
questions_correct = 0
questions_wrong = 0

def play_sounds(sound_2_play):
    while sound_2_play.get_busy():
        pass

ask_questions = input('Ask another Question (1/2/0) :')

while int(ask_questions) != 0:
    if int(ask_questions) == 1:
        questions_correct += 1
        questions_number += 1
        s1 = sounds.Sound('Sounds/correct.wav')
        play_sounds(s1.play())

    else:
        questions_wrong += 1
        questions_number += 1
        s2 = sounds.Sound('Sounds/wrong.wav')
        play_sounds(s2.play())

    ask_questions = input('Ask another Question (1/2/0) :')

print('Total number of questions: ' + str(questions_number))
print('Number of correct questions: ' + str(questions_correct))
print('Number of wrong questions: ' + str(questions_wrong))

