# -*- coding: utf-8 -*-
"""Contenu pédagogique original lié aux thèmes du manuel Developing Chinese, Elementary Speaking Course I.
La progression thématique et les pages sont fondées sur le sommaire du PDF fourni ;
les dialogues, explications et exercices sont rédigés pour cette application, sans transcrire intégralement le manuel.
"""
import json, os, re
from pathlib import Path
L=[]
def add(num,hanzi,title,en,page,goal,vocab,grammar,dialog1,dialog2,pronunciation,task):
 def rows(t,expected):
  out=[]
  for line in t.strip().split('\n'):
   if not line.strip(): continue
   parts=[s.strip() for s in line.strip().split('|')]
   if len(parts)!=expected: raise ValueError((num,expected,parts))
   out.append(parts)
  return out
 words=[dict(zh=z,py=p,fr=f) for z,p,f in rows(vocab,3)]
 gr=[dict(title=a,explanation=b,zh=c,py=d,fr=e) for a,b,c,d,e in rows(grammar,5)]
 dialogs=[]
 for title0,situation,tx in [dialog1,dialog2]:
  dialogs.append(dict(title=title0,context=situation,lines=[dict(speaker=s,zh=z,py=p,fr=f) for s,z,p,f in rows(tx,4)]))
 L.append(dict(id=num,hanzi=hanzi,title=title,en=en,sourcePage=page,goal=goal,vocab=words,grammar=gr,dialogs=dialogs,pronunciation=pronunciation,mission=task))

add(1,'你好','Bonjour !','Hello',1,
'Saluer, prendre congé, distinguer les quatre tons et le ton neutre.',
'''你|nǐ|tu / vous
好|hǎo|bien / bon
你好|nǐ hǎo|bonjour
您|nín|vous (poli)
您好|nín hǎo|bonjour (poli)
你们|nǐmen|vous (pluriel)
老师|lǎoshī|professeur
同学|tóngxué|camarade de classe
早上好|zǎoshang hǎo|bonjour (matin)
下午好|xiàwǔ hǎo|bon après-midi
晚上好|wǎnshang hǎo|bonsoir
再见|zàijiàn|au revoir
我|wǒ|je / moi
们|men|suffixe pluriel de personne
朋友|péngyou|ami
大家|dàjiā|tout le monde
谢谢|xièxie|merci
认识|rènshi|faire connaissance
中国|Zhōngguó|Chine
汉语|Hànyǔ|langue chinoise''',
'''Salutation simple|你好 est la formule de base. Le second caractère 好 porte le troisième ton ; la combinaison change légèrement en discours.|你好！|Nǐ hǎo!|Bonjour !
Politesse avec 您|您 est une forme respectueuse de 你, notamment envers un professeur ou une personne plus âgée.|老师，您好！|Lǎoshī, nín hǎo!|Bonjour, professeur !
Pluriel des pronoms|Le suffixe 们 se combine avec 你 / 我 / 他 lorsqu’on parle d’un groupe de personnes.|你们好！|Nǐmen hǎo!|Bonjour à vous tous !''',
('Rencontre en classe','Deux camarades arrivent à l’école.','''A|你好！|Nǐ hǎo!|Bonjour !
B|你好！|Nǐ hǎo!|Bonjour !
A|你是新同学吗？|Nǐ shì xīn tóngxué ma?|Tu es un nouvel élève ?
B|是的。很高兴认识你！|Shì de. Hěn gāoxìng rènshi nǐ!|Oui. Ravi de te rencontrer !
A|我也很高兴！|Wǒ yě hěn gāoxìng!|Moi aussi, je suis ravi !
B|再见！|Zàijiàn!|Au revoir !'''),
('Avec une enseignante','Dans le couloir avant le cours.','''A|老师，早上好！|Lǎoshī, zǎoshang hǎo!|Bonjour, professeur !
B|早上好！|Zǎoshang hǎo!|Bonjour !
A|老师，您好吗？|Lǎoshī, nín hǎo ma?|Professeur, comment allez-vous ?
B|我很好，谢谢。|Wǒ hěn hǎo, xièxie.|Je vais très bien, merci.
A|老师，再见！|Lǎoshī, zàijiàn!|Au revoir, professeur !
B|再见！|Zàijiàn!|Au revoir !'''),
'Entraîne-toi sur mā, má, mǎ, mà, puis sur le ton neutre de men. Attention au troisième ton de nǐ hǎo.',
'Salue un professeur et deux camarades ; termine les trois échanges par une formule de départ.')

add(2,'谢谢','Merci','Thank you',8,
'Remercier, répondre à une excuse et maîtriser les changements de ton de 不 et du troisième ton.',
'''谢谢|xièxie|merci
不客气|bú kèqi|de rien
对不起|duìbuqǐ|pardon / désolé
没关系|méi guānxi|ce n’est pas grave
不用谢|bú yòng xiè|pas de quoi
不用|bú yòng|pas nécessaire
不|bù|ne… pas
是|shì|être / oui
早上|zǎoshang|matin
中午|zhōngwǔ|midi
下午|xiàwǔ|après-midi
晚上|wǎnshang|soir
你好|nǐ hǎo|bonjour
晚安|wǎn’ān|bonne nuit
请|qǐng|s’il vous plaît
帮助|bāngzhù|aider
没|méi|ne pas avoir
问题|wèntí|problème
可以|kěyǐ|pouvoir / possible
今天|jīntiān|aujourd’hui''',
'''Répondre à merci|On répond souvent à 谢谢 par 不客气 ou 不用谢.|谢谢！不客气！|Xièxie! Bú kèqi!|Merci ! De rien !
S’excuser|对不起 introduit une excuse ; 没关系 rassure la personne.|对不起！没关系。|Duìbuqǐ! Méi guānxi.|Pardon ! Ce n’est pas grave.
Changement de ton de 不|不 (bù) se prononce souvent bú devant une syllabe au quatrième ton, par exemple 客 kè.|不客气。|Bú kèqi.|De rien.''',
('Remercier pour une aide','Un cahier vient de tomber.','''A|这是你的书吗？|Zhè shì nǐ de shū ma?|C’est ton livre ?
B|是的，谢谢！|Shì de, xièxie!|Oui, merci !
A|不客气。|Bú kèqi.|De rien.
B|你真好！|Nǐ zhēn hǎo!|Tu es vraiment gentil !
A|没关系，我们是朋友。|Méi guānxi, wǒmen shì péngyou.|De rien, nous sommes amis.'''),
('Petite collision','Dans le couloir.','''A|对不起！|Duìbuqǐ!|Pardon !
B|没关系。|Méi guānxi.|Ce n’est pas grave.
A|谢谢你！|Xièxie nǐ!|Merci à toi !
B|不用谢。|Bú yòng xiè.|Il n’y a pas de quoi.
A|再见！|Zàijiàn!|Au revoir !'''),
'Répète nǐ hǎo et hěn hǎo pour le troisième ton, puis compare bù shì et bú kèqi.',
'Imagine trois situations : cadeau reçu, aide rendue et excuse à présenter.')

add(3,'今天是星期一','Aujourd’hui, c’est lundi','Today is Monday',14,
'Dire le jour, la date, demander un rendez-vous, pratiquer les nombres et le changement de ton de 一.',
'''今天|jīntiān|aujourd’hui
明天|míngtiān|demain
昨天|zuótiān|hier
星期|xīngqī|semaine
星期一|xīngqīyī|lundi
星期二|xīngqī’èr|mardi
星期三|xīngqīsān|mercredi
星期四|xīngqīsì|jeudi
星期五|xīngqīwǔ|vendredi
星期六|xīngqīliù|samedi
星期天|xīngqītiān|dimanche
月|yuè|mois
号|hào|jour du mois (oral)
日|rì|jour (écrit)
几|jǐ|combien (petit nombre)
几号|jǐ hào|quel jour du mois
几月|jǐ yuè|quel mois
八|bā|huit
九|jiǔ|neuf
十|shí|dix
一|yī|un
二|èr|deux
三|sān|trois''',
'''Dire le jour de semaine|On utilise 星期 suivi d’un nombre pour les jours du lundi au samedi.|今天是星期一。|Jīntiān shì xīngqīyī.|Aujourd’hui, c’est lundi.
Demander la date|几月几号 sert à demander le mois et le jour. Le mois précède le jour.|今天几月几号？|Jīntiān jǐ yuè jǐ hào?|Quelle est la date aujourd’hui ?
Changement de ton de 一|一 change souvent selon le ton suivant ; il peut se prononcer yí, yì ou yī selon le contexte.|一个人。|Yí ge rén.|Une personne.''',
('Prévoir une visite','Deux amis parlent de leur emploi du temps.','''A|今天星期几？|Jīntiān xīngqī jǐ?|On est quel jour aujourd’hui ?
B|今天星期一。|Jīntiān xīngqīyī.|Aujourd’hui, c’est lundi.
A|明天星期二吗？|Míngtiān xīngqī’èr ma?|Demain, c’est mardi ?
B|对，明天星期二。|Duì, míngtiān xīngqī’èr.|Oui, demain, c’est mardi.
A|星期三有时间吗？|Xīngqīsān yǒu shíjiān ma?|Tu as du temps mercredi ?
B|有，我们星期三见！|Yǒu, wǒmen xīngqīsān jiàn!|Oui, à mercredi !'''),
('À l’accueil','Vérifier la date d’un événement.','''A|请问，今天几月几号？|Qǐngwèn, jīntiān jǐ yuè jǐ hào?|Excusez-moi, quelle est la date ?
B|今天是九月八号。|Jīntiān shì jiǔ yuè bā hào.|Nous sommes le 8 septembre.
A|明天是九号吗？|Míngtiān shì jiǔ hào ma?|Demain, c’est le 9 ?
B|是的，明天九号。|Shì de, míngtiān jiǔ hào.|Oui, demain le 9.
A|谢谢！|Xièxie!|Merci !'''),
'Entraîne-toi aux nombres de 1 à 31, aux jours de la semaine et aux variations de 一.',
'Donne la date du jour, celle de demain et propose un rendez-vous pour la semaine prochaine.')

add(4,'我是中国人','Je suis chinois','I’m Chinese',20,
'Se présenter, exprimer sa nationalité, demander le nom d’une personne et nouer une relation.',
'''我|wǒ|je
你|nǐ|tu
他|tā|il
她|tā|elle
我们|wǒmen|nous
是|shì|être
中国|Zhōngguó|Chine
中国人|Zhōngguó rén|Chinois / Chinoise
法国|Fǎguó|France
法国人|Fǎguó rén|Français / Française
英国|Yīngguó|Royaume-Uni
美国|Měiguó|États-Unis
韩国|Hánguó|Corée du Sud
名字|míngzi|prénom / nom
姓|xìng|porter le nom de famille
叫|jiào|s’appeler
人|rén|personne
朋友|péngyou|ami
认识|rènshi|connaître
很|hěn|très / lien avec adjectif
高兴|gāoxìng|content
也|yě|aussi
哪里|nǎlǐ|où
哪国|nǎ guó|quel pays''',
'''Identité avec 是|On associe sujet et identité par 是, sans article avant les noms de nationalité.|我是中国人。|Wǒ shì Zhōngguó rén.|Je suis chinois.
Présenter son nom|Pour dire comment on s’appelle, on emploie 我叫 suivi du nom.|我叫李雪。|Wǒ jiào Lǐ Xuě.|Je m’appelle Li Xue.
Mettre 也 avant le verbe|也 (aussi) précède généralement le verbe ou l’adjectif auquel il se rapporte.|我也是学生。|Wǒ yě shì xuéshēng.|Je suis aussi étudiant.''',
('Faire connaissance','Deux nouveaux étudiants discutent.','''A|你好！你叫什么名字？|Nǐ hǎo! Nǐ jiào shénme míngzi?|Bonjour ! Comment t’appelles-tu ?
B|我叫安娜。你呢？|Wǒ jiào Ānnà. Nǐ ne?|Je m’appelle Anna. Et toi ?
A|我叫大卫。你是哪国人？|Wǒ jiào Dàwèi. Nǐ shì nǎ guó rén?|Je m’appelle David. Tu es de quelle nationalité ?
B|我是法国人。你呢？|Wǒ shì Fǎguó rén. Nǐ ne?|Je suis française. Et toi ?
A|我是中国人。|Wǒ shì Zhōngguó rén.|Je suis chinois.
B|认识你很高兴！|Rènshi nǐ hěn gāoxìng!|Enchantée de te connaître !'''),
('Présenter une amie','À une rencontre entre étudiants.','''A|她是谁？|Tā shì shéi?|Qui est-elle ?
B|她是我朋友。|Tā shì wǒ péngyou.|C’est mon amie.
A|她叫什么名字？|Tā jiào shénme míngzi?|Comment s’appelle-t-elle ?
B|她叫玛丽。|Tā jiào Mǎlì.|Elle s’appelle Marie.
A|她也是学生吗？|Tā yě shì xuéshēng ma?|Elle est aussi étudiante ?
B|对，她也是学生。|Duì, tā yě shì xuéshēng.|Oui, elle est aussi étudiante.'''),
'Travaille les enchaînements du troisième ton dans nǐ hǎo et rènshi nǐ, ainsi que la terminaison -r de nǎr.',
'Présente-toi : nom, pays, statut et une personne de ton entourage.')

add(5,'我学习汉语','J’étudie le chinois','I study Chinese',30,
'Demander le nom, les langues étudiées, les activités et la profession des personnes.',
'''学习|xuéxí|étudier
汉语|Hànyǔ|chinois (langue)
中文|Zhōngwén|chinois écrit ou parlé
英语|Yīngyǔ|anglais
法语|Fǎyǔ|français
老师|lǎoshī|professeur
学生|xuéshēng|élève / étudiant
什么|shénme|quoi / quel
名字|míngzi|nom
哪|nǎ|quel
国|guó|pays
谁|shéi|qui
吗|ma|particule interrogative
呢|ne|particule de relance
专业|zhuānyè|spécialité
经济|jīngjì|économie
工作|gōngzuò|travailler / travail
医生|yīshēng|médecin
律师|lǜshī|avocat
同学|tóngxué|camarade
不|bù|ne… pas
说|shuō|parler
会|huì|savoir / pouvoir
一点儿|yìdiǎnr|un peu''',
'''Question par mot interrogatif|On remplace l’élément inconnu par 什么, 谁 ou 哪, à sa position habituelle dans la phrase.|你学习什么？|Nǐ xuéxí shénme?|Qu’étudies-tu ?
Oui/non avec 吗|En ajoutant 吗 à la fin d’une phrase affirmative, on pose une question fermée.|你是老师吗？|Nǐ shì lǎoshī ma?|Es-tu professeur ?
Relance avec 呢|呢 permet de poser à son tour une question dont le contexte est connu.|我学习汉语。你呢？|Wǒ xuéxí Hànyǔ. Nǐ ne?|J’étudie le chinois. Et toi ?''',
('Premier cours de langue','Une étudiante découvre son voisin.','''A|你好！你学习什么？|Nǐ hǎo! Nǐ xuéxí shénme?|Bonjour ! Qu’est-ce que tu étudies ?
B|我学习汉语。|Wǒ xuéxí Hànyǔ.|J’étudie le chinois.
A|你会说汉语吗？|Nǐ huì shuō Hànyǔ ma?|Sais-tu parler chinois ?
B|我会说一点儿。|Wǒ huì shuō yìdiǎnr.|J’en parle un peu.
A|我学习英语。|Wǒ xuéxí Yīngyǔ.|J’étudie l’anglais.
B|认识你很高兴！|Rènshi nǐ hěn gāoxìng!|Ravi de te connaître !'''),
('Interroger sur une profession','À une fête universitaire.','''A|请问，他是谁？|Qǐngwèn, tā shì shéi?|Excuse-moi, qui est-il ?
B|他是我们的老师。|Tā shì wǒmen de lǎoshī.|C’est notre professeur.
A|他教什么？|Tā jiāo shénme?|Qu’enseigne-t-il ?
B|他教汉语。|Tā jiāo Hànyǔ.|Il enseigne le chinois.
A|你也是学生吗？|Nǐ yě shì xuéshēng ma?|Es-tu aussi étudiant ?
B|是的，我学习经济。|Shì de, wǒ xuéxí jīngjì.|Oui, j’étudie l’économie.'''),
'Entraîne-toi à distinguer x / sh, j / zh et les sons de xuéxí ; prononce correctement shénme et shéi.',
'Interroge un partenaire sur son nom, son pays, sa langue et ses études puis présente-le.')

add(6,'你们班有多少人','Combien d’élèves dans votre classe ?','How many people are there in your class',38,
'Présenter sa famille et sa classe, compter les personnes, utiliser 有, 没有 et les classificateurs.',
'''班|bān|classe
人|rén|personne
学生|xuéshēng|étudiant
男生|nánshēng|garçon / étudiant
女生|nǚshēng|fille / étudiante
多少|duōshao|combien
几|jǐ|combien (petit nombre)
个|ge|classificateur général
有|yǒu|avoir / il y a
没有|méiyǒu|ne pas avoir
家|jiā|famille / foyer
哥哥|gēge|grand frère
弟弟|dìdi|petit frère
姐姐|jiějie|grande sœur
妹妹|mèimei|petite sœur
爸爸|bàba|papa
妈妈|māma|maman
口|kǒu|classificateur des membres du foyer
还|hái|encore / en plus
一共|yígòng|au total
对|duì|exact / juste
两|liǎng|deux (devant classificateur)
二十|èrshí|vingt
同学|tóngxué|camarade de classe''',
'''Exprimer la possession|有 indique une possession ou une existence ; sa négation est 没有.|我有一个姐姐。|Wǒ yǒu yí ge jiějie.|J’ai une grande sœur.
Demander une quantité|几 s’utilise plutôt pour de petits nombres ; 多少 est courant pour une quantité inconnue.|你们班有多少人？|Nǐmen bān yǒu duōshao rén?|Combien de personnes y a-t-il dans votre classe ?
Classificateurs|Le classificateur est requis entre un nombre et un nom : 两个学生, 三口人.|我家有四口人。|Wǒ jiā yǒu sì kǒu rén.|Nous sommes quatre dans ma famille.''',
('Parler de sa classe','Les camarades comptent les présents.','''A|你们班有多少人？|Nǐmen bān yǒu duōshao rén?|Combien d’élèves dans votre classe ?
B|我们班有二十个人。|Wǒmen bān yǒu èrshí ge rén.|Nous sommes vingt.
A|有几个女生？|Yǒu jǐ ge nǚshēng?|Combien de filles ?
B|有十二个女生。|Yǒu shí’èr ge nǚshēng.|Douze filles.
A|还有几个男生？|Hái yǒu jǐ ge nánshēng?|Et combien de garçons ?
B|有八个男生。|Yǒu bā ge nánshēng.|Huit garçons.'''),
('Présenter sa famille','Deux amis regardent une photo.','''A|你家有几口人？|Nǐ jiā yǒu jǐ kǒu rén?|Combien de personnes dans ta famille ?
B|我家有五口人。|Wǒ jiā yǒu wǔ kǒu rén.|Nous sommes cinq.
A|你有哥哥吗？|Nǐ yǒu gēge ma?|As-tu un grand frère ?
B|没有，我有一个姐姐。|Méiyǒu, wǒ yǒu yí ge jiějie.|Non, j’ai une grande sœur.
A|这是谁？|Zhè shì shéi?|Qui est-ce ?
B|这是我妈妈。|Zhè shì wǒ māma.|C’est ma mère.'''),
'Compare rén / réng et nǚ / nǔ, ainsi que liǎng ge et èrshí ge.',
'Présente ta famille et fais le total de filles, garçons et élèves de ta classe.')

add(7,'一共多少钱','Combien coûte le tout ?','How much altogether',48,
'Faire des achats, demander les prix, utiliser 要, 想, 多少钱, les montants en 元 / 块 / 毛 / 分.',
'''一共|yígòng|en tout
多少|duōshao|combien
钱|qián|argent
多少钱|duōshao qián|combien ça coûte
买|mǎi|acheter
卖|mài|vendre
要|yào|vouloir / avoir besoin
想|xiǎng|souhaiter
元|yuán|yuan (unité monétaire)
块|kuài|yuan (oral)
毛|máo|dixième de yuan
角|jiǎo|dixième de yuan
分|fēn|centième de yuan
一瓶|yì píng|une bouteille de
瓶|píng|bouteille
杯|bēi|verre / tasse
水|shuǐ|eau
面包|miànbāo|pain
葡萄|pútao|raisin
苹果|píngguǒ|pomme
公斤|gōngjīn|kilogramme
斤|jīn|demi-kilo (500 g)
贵|guì|cher
便宜|piányi|bon marché
找|zhǎo|rendre la monnaie
再|zài|encore / en plus''',
'''Vouloir acheter|想 indique un souhait ; 要 peut exprimer la demande d’un article.|我想买苹果。|Wǒ xiǎng mǎi píngguǒ.|Je voudrais acheter des pommes.
Prix et monnaie|多少钱 introduit une question de prix ; à l’oral, 块 et 毛 sont courants.|一共十八块五。|Yígòng shíbā kuài wǔ.|Ça fait 18 yuans et 50 centimes.
Classificateur de contenant|On combine le nombre et un classificateur adapté au produit.|我要两瓶水。|Wǒ yào liǎng píng shuǐ.|Je voudrais deux bouteilles d’eau.''',
('À l’épicerie','Une étudiante achète des provisions.','''A|你好！你要什么？|Nǐ hǎo! Nǐ yào shénme?|Bonjour ! Que souhaitez-vous ?
B|我要两瓶水和一个面包。|Wǒ yào liǎng píng shuǐ hé yí ge miànbāo.|Deux bouteilles d’eau et un pain.
A|还要什么？|Hái yào shénme?|Autre chose ?
B|再要一斤苹果。|Zài yào yì jīn píngguǒ.|Encore un demi-kilo de pommes.
A|一共二十五块。|Yígòng èrshíwǔ kuài.|Cela fait 25 yuans.
B|给你，谢谢。|Gěi nǐ, xièxie.|Tenez, merci.'''),
('Comparer les prix','Au marché.','''A|苹果多少钱一斤？|Píngguǒ duōshao qián yì jīn?|Combien le demi-kilo de pommes ?
B|八块钱一斤。|Bā kuài qián yì jīn.|Huit yuans le demi-kilo.
A|有点儿贵。|Yǒudiǎnr guì.|C’est un peu cher.
B|这个便宜，六块。|Zhège piányi, liù kuài.|Celles-ci sont moins chères : six yuans.
A|好，我买一斤。|Hǎo, wǒ mǎi yì jīn.|D’accord, j’en prends un demi-kilo.
B|好的，给你。|Hǎo de, gěi nǐ.|Bien, les voici.'''),
'Compare mǎi « acheter » (3e ton) et mài « vendre » (4e ton). Pratique yí gòng et yì píng.',
'Joue un achat de trois articles, demande le montant total et fais rendre la monnaie.')

add(8,'请问，银行在哪儿','Excusez-moi, où est la banque ?','Excuse me, where’s the bank',60,
'Demander son chemin, identifier des lieux, employer 在, 哪儿, les repères et les directions.',
'''请问|qǐngwèn|excusez-moi / puis-je demander
银行|yínháng|banque
在哪儿|zài nǎr|où se trouve
哪儿|nǎr|où
在|zài|à / se trouver
这儿|zhèr|ici
那儿|nàr|là-bas
学校|xuéxiào|école
图书馆|túshūguǎn|bibliothèque
医院|yīyuàn|hôpital
超市|chāoshì|supermarché
饭馆|fànguǎn|restaurant
前面|qiánmiàn|devant
后面|hòumiàn|derrière
左边|zuǒbian|à gauche
右边|yòubian|à droite
旁边|pángbiān|à côté
对面|duìmiàn|en face
附近|fùjìn|près d’ici
一直|yìzhí|tout droit
走|zǒu|marcher / aller
拐|guǎi|tourner
远|yuǎn|loin
近|jìn|près''',
'''Localiser avec 在|Le schéma sujet + 在 + lieu permet d’indiquer une localisation.|银行在学校旁边。|Yínháng zài xuéxiào pángbiān.|La banque est à côté de l’école.
Demander un emplacement|哪儿 occupe la place du lieu inconnu, généralement après 在.|银行在哪儿？|Yínháng zài nǎr?|Où est la banque ?
Indiquer la direction|On combine 一直走 et 向左 / 向右拐 pour guider une personne.|一直走，然后向右拐。|Yìzhí zǒu, ránhòu xiàng yòu guǎi.|Allez tout droit puis tournez à droite.''',
('Chercher la banque','Dans la rue.','''A|请问，银行在哪儿？|Qǐngwèn, yínháng zài nǎr?|Excusez-moi, où est la banque ?
B|银行在超市旁边。|Yínháng zài chāoshì pángbiān.|Elle est à côté du supermarché.
A|离这儿远吗？|Lí zhèr yuǎn ma?|C’est loin d’ici ?
B|不远，一直走。|Bù yuǎn, yìzhí zǒu.|Non, allez tout droit.
A|然后呢？|Ránhòu ne?|Et ensuite ?
B|向左拐就到了。|Xiàng zuǒ guǎi jiù dào le.|Tournez à gauche et vous y serez.'''),
('Dans le campus','Un étudiant cherche une bibliothèque.','''A|图书馆在哪儿？|Túshūguǎn zài nǎr?|Où est la bibliothèque ?
B|在教学楼后面。|Zài jiàoxuélóu hòumiàn.|Derrière le bâtiment des cours.
A|医院在附近吗？|Yīyuàn zài fùjìn ma?|L’hôpital est près d’ici ?
B|不，医院比较远。|Bù, yīyuàn bǐjiào yuǎn.|Non, l’hôpital est assez loin.
A|谢谢你的帮助！|Xièxie nǐ de bāngzhù!|Merci de ton aide !
B|不客气！|Bú kèqi!|De rien !'''),
'Entraîne-toi aux sons rétroflexes zh, ch, sh dans zhèr, chāoshì et shū.',
'Décris le chemin entre ton école et une banque fictive avec au moins trois indications spatiales.')

add(9,'今天几月几号','Nous sommes quel jour du mois ?','What’s the date today',71,
'Exprimer dates précises, anniversaires, années, semaines et heures de rendez-vous.',
'''日期|rìqī|date
今天|jīntiān|aujourd’hui
昨天|zuótiān|hier
明天|míngtiān|demain
后天|hòutiān|après-demain
年|nián|année
月|yuè|mois
号|hào|jour du mois
星期|xīngqī|semaine
生日|shēngrì|anniversaire
什么时候|shénme shíhou|quand
几号|jǐ hào|le combien
今年|jīnnián|cette année
去年|qùnián|l’année passée
明年|míngnián|l’année prochaine
参加|cānjiā|participer
聚会|jùhuì|fête / réunion
星期天|xīngqītiān|dimanche
上午|shàngwǔ|matinée
下午|xiàwǔ|après-midi
见面|jiànmiàn|se voir
有空|yǒu kòng|être libre
祝|zhù|souhaiter
快乐|kuàilè|heureux / joyeux''',
'''Ordre des dates|En chinois, l’ordre est année + mois + jour, du plus grand au plus petit.|今天是五月十号。|Jīntiān shì wǔ yuè shí hào.|Aujourd’hui, c’est le 10 mai.
Demander « quand »|什么时候 s’utilise pour interroger le moment d’un événement.|你什么时候有空？|Nǐ shénme shíhou yǒu kòng?|Quand es-tu libre ?
Anniversaire|生日快乐 est le souhait classique pour un anniversaire.|祝你生日快乐！|Zhù nǐ shēngrì kuàilè!|Joyeux anniversaire !''',
('Anniversaire','Deux amies préparent une fête.','''A|你的生日是几月几号？|Nǐ de shēngrì shì jǐ yuè jǐ hào?|C’est quand ton anniversaire ?
B|五月十号。|Wǔ yuè shí hào.|Le 10 mai.
A|今年是星期几？|Jīnnián shì xīngqī jǐ?|Cette année, ça tombe quel jour ?
B|是星期天。|Shì xīngqītiān.|C’est dimanche.
A|我们一起吃饭吧！|Wǒmen yìqǐ chīfàn ba!|Allons manger ensemble !
B|好啊，谢谢你！|Hǎo a, xièxie nǐ!|Bonne idée, merci !'''),
('Préparer une rencontre','Organiser un rendez-vous.','''A|你什么时候有空？|Nǐ shénme shíhou yǒu kòng?|Quand es-tu disponible ?
B|星期六下午有空。|Xīngqīliù xiàwǔ yǒu kòng.|Samedi après-midi.
A|我们三点见面，好吗？|Wǒmen sān diǎn jiànmiàn, hǎo ma?|On se voit à trois heures ?
B|可以，在哪儿见？|Kěyǐ, zài nǎr jiàn?|D’accord, où ?
A|在图书馆门口。|Zài túshūguǎn ménkǒu.|Devant la bibliothèque.
B|好，星期六见！|Hǎo, xīngqīliù jiàn!|Bien, à samedi !'''),
'Prononce les nombres composés et l’enchaînement des dates : wǔ yuè shí hào.',
'Donne ta date d’anniversaire et organise un rendez-vous en mentionnant date, heure et lieu.')

add(10,'我每天八点上课','J’ai cours tous les jours à huit heures','I have class at 8 o’clock every day',82,
'Décrire un emploi du temps, les heures, la fréquence et les activités quotidiennes.',
'''每天|měitiān|chaque jour
早上|zǎoshang|matin
起床|qǐchuáng|se lever
洗澡|xǐzǎo|prendre une douche
吃饭|chīfàn|manger
早饭|zǎofàn|petit déjeuner
午饭|wǔfàn|déjeuner
晚饭|wǎnfàn|dîner
上课|shàngkè|avoir cours
下课|xiàkè|finir un cours
上学|shàngxué|aller à l’école
睡觉|shuìjiào|dormir
点|diǎn|heure (sur l’horloge)
分|fēn|minute
半|bàn|demie
刻|kè|quart d’heure
分钟|fēnzhōng|minute (durée)
现在|xiànzài|maintenant
经常|jīngcháng|souvent
有时候|yǒu shíhou|parfois
一般|yìbān|en général
晚上|wǎnshang|soir
做作业|zuò zuòyè|faire les devoirs
休息|xiūxi|se reposer''',
'''Heure avant l’action|Le complément de temps se place généralement avant le verbe.|我每天八点上课。|Wǒ měitiān bā diǎn shàngkè.|J’ai cours chaque jour à huit heures.
Exprimer la demie|点半 signifie une heure et demie.|我七点半起床。|Wǒ qī diǎn bàn qǐchuáng.|Je me lève à 7 h 30.
Fréquence|每天 / 经常 / 有时候 indiquent différentes fréquences, en général avant le verbe.|我有时候晚上学习。|Wǒ yǒu shíhou wǎnshang xuéxí.|J’étudie parfois le soir.''',
('Routine du matin','Deux étudiants comparent leurs habitudes.','''A|你每天几点起床？|Nǐ měitiān jǐ diǎn qǐchuáng?|À quelle heure te lèves-tu chaque jour ?
B|我七点起床。|Wǒ qī diǎn qǐchuáng.|À sept heures.
A|你几点吃早饭？|Nǐ jǐ diǎn chī zǎofàn?|À quelle heure prends-tu ton petit déjeuner ?
B|七点半。|Qī diǎn bàn.|À sept heures et demie.
A|你几点上课？|Nǐ jǐ diǎn shàngkè?|À quelle heure as-tu cours ?
B|我八点上课。|Wǒ bā diǎn shàngkè.|J’ai cours à huit heures.'''),
('Après les cours','Parler de la soirée.','''A|你晚上做什么？|Nǐ wǎnshang zuò shénme?|Que fais-tu le soir ?
B|我一般做作业。|Wǒ yìbān zuò zuòyè.|En général, je fais mes devoirs.
A|你经常看电视吗？|Nǐ jīngcháng kàn diànshì ma?|Regardes-tu souvent la télévision ?
B|不经常，我有时候看书。|Bù jīngcháng, wǒ yǒu shíhou kàn shū.|Pas souvent, je lis parfois.
A|你几点睡觉？|Nǐ jǐ diǎn shuìjiào?|À quelle heure te couches-tu ?
B|十一点左右。|Shíyī diǎn zuǒyòu.|Vers onze heures.'''),
'Pratique qī diǎn, qī diǎn bàn, bā diǎn yí kè et les contrastes diǎn / tiān.',
'Décris une journée type avec au moins cinq heures et trois adverbes de fréquence.')

add(11,'我住在留学生宿舍','J’habite au dortoir des étudiants étrangers','I stay in the International Student Dormitory',95,
'Indiquer son adresse, sa chambre, son logement ; poser des questions de localisation et de possession.',
'''住|zhù|habiter
住在|zhù zài|habiter à
宿舍|sùshè|dortoir
留学生|liúxuéshēng|étudiant étranger
房间|fángjiān|chambre
楼|lóu|étage / bâtiment
层|céng|étage
号|hào|numéro
几|jǐ|combien / quel numéro
有|yǒu|avoir
没有|méiyǒu|ne pas avoir
室友|shìyǒu|colocataire
床|chuáng|lit
桌子|zhuōzi|table / bureau
椅子|yǐzi|chaise
门|mén|porte
窗户|chuānghu|fenêtre
卫生间|wèishēngjiān|salle de bains / toilettes
厨房|chúfáng|cuisine
干净|gānjìng|propre
大|dà|grand
小|xiǎo|petit
方便|fāngbiàn|pratique
离|lí|être distant de''',
'''Habiter à|住在 associe habiter et le lieu de résidence.|我住在学生宿舍。|Wǒ zhù zài xuéshēng sùshè.|J’habite au dortoir des étudiants.
Numéro de pièce|Pour décrire un étage ou une chambre, on combine les nombres avec 楼 / 层 / 号.|我住在三楼。|Wǒ zhù zài sān lóu.|J’habite au troisième étage.
Existence dans un lieu|Lieu + 有 + objet indique ce qui se trouve à cet endroit.|房间里有两张床。|Fángjiān li yǒu liǎng zhāng chuáng.|Il y a deux lits dans la chambre.''',
('Une nouvelle chambre','Un étudiant demande où vit son ami.','''A|你住在哪儿？|Nǐ zhù zài nǎr?|Où habites-tu ?
B|我住在留学生宿舍。|Wǒ zhù zài liúxuéshēng sùshè.|Au dortoir des étudiants étrangers.
A|你住几楼？|Nǐ zhù jǐ lóu?|À quel étage ?
B|三楼，三零二号房间。|Sān lóu, sān líng èr hào fángjiān.|Au troisième, chambre 302.
A|你的房间大吗？|Nǐ de fángjiān dà ma?|Ta chambre est grande ?
B|不大，但是很干净。|Bú dà, dànshì hěn gānjìng.|Non, mais elle est propre.'''),
('Visite du dortoir','Un camarade découvre la chambre.','''A|请进！这是我的房间。|Qǐng jìn! Zhè shì wǒ de fángjiān.|Entre ! Voici ma chambre.
B|房间里有几张床？|Fángjiān li yǒu jǐ zhāng chuáng?|Combien de lits y a-t-il ?
A|有两张床和一张桌子。|Yǒu liǎng zhāng chuáng hé yì zhāng zhuōzi.|Deux lits et un bureau.
B|你有室友吗？|Nǐ yǒu shìyǒu ma?|As-tu un colocataire ?
A|有，他也是留学生。|Yǒu, tā yě shì liúxuéshēng.|Oui, il est également étudiant étranger.
B|这里很方便。|Zhèlǐ hěn fāngbiàn.|C’est très pratique ici.'''),
'Pratique les syllabes zhù, zhāng, chuáng et les oppositions c / ch et z / zh.',
'Décris ta chambre : étage, numéro, mobilier, colocataire et qualités du logement.')

add(12,'我在北京学习汉语','J’étudie le chinois à Pékin','I study Chinese in Beijing',108,
'Décrire ses études, activités, lieux et moyens de transport, introduire 在 + lieu + verbe et 去.',
'''北京|Běijīng|Pékin
在|zài|à / dans
学习|xuéxí|étudier
大学|dàxué|université
汉语|Hànyǔ|langue chinoise
汉字|Hànzì|caractère chinois
口语|kǒuyǔ|expression orale
听力|tīnglì|compréhension orale
老师|lǎoshī|enseignant
教室|jiàoshì|salle de classe
图书馆|túshūguǎn|bibliothèque
练习|liànxí|s’entraîner
读|dú|lire
写|xiě|écrire
听|tīng|écouter
说|shuō|parler
去|qù|aller
来|lái|venir
坐|zuò|prendre (transport)
公共汽车|gōnggòng qìchē|bus
地铁|dìtiě|métro
骑自行车|qí zìxíngchē|aller à vélo
一起|yìqǐ|ensemble
常常|chángcháng|souvent''',
'''Lieu avant le verbe|Pour une action accomplie dans un endroit, 在 + lieu précède le verbe principal.|我在北京学习汉语。|Wǒ zài Běijīng xuéxí Hànyǔ.|J’étudie le chinois à Pékin.
Aller faire quelque chose|去 se combine avec un lieu, puis éventuellement une activité.|我去图书馆看书。|Wǒ qù túshūguǎn kàn shū.|Je vais à la bibliothèque lire.
Transport avec 坐|坐 précède le moyen de transport et peut être associé à 去.|我坐地铁去学校。|Wǒ zuò dìtiě qù xuéxiào.|Je prends le métro pour aller à l’école.''',
('Étudier à Pékin','Deux étudiants parlent de leurs activités.','''A|你在哪儿学习汉语？|Nǐ zài nǎr xuéxí Hànyǔ?|Où étudies-tu le chinois ?
B|我在北京大学学习汉语。|Wǒ zài Běijīng Dàxué xuéxí Hànyǔ.|À l’université de Pékin.
A|你每天练习口语吗？|Nǐ měitiān liànxí kǒuyǔ ma?|Pratiques-tu l’oral chaque jour ?
B|对，我常常跟朋友说汉语。|Duì, wǒ chángcháng gēn péngyou shuō Hànyǔ.|Oui, je parle souvent chinois avec des amis.
A|你也练习写汉字吗？|Nǐ yě liànxí xiě Hànzì ma?|Pratiques-tu aussi l’écriture ?
B|当然，我每天写汉字。|Dāngrán, wǒ měitiān xiě Hànzì.|Bien sûr, chaque jour.'''),
('Se rendre en cours','Avant de partir de la résidence.','''A|你怎么去学校？|Nǐ zěnme qù xuéxiào?|Comment vas-tu à l’école ?
B|我坐地铁去。|Wǒ zuò dìtiě qù.|Je prends le métro.
A|你今天去哪儿？|Nǐ jīntiān qù nǎr?|Où vas-tu aujourd’hui ?
B|我去图书馆看书。|Wǒ qù túshūguǎn kàn shū.|Je vais lire à la bibliothèque.
A|我们一起去吧！|Wǒmen yìqǐ qù ba!|Allons-y ensemble !
B|好，走吧！|Hǎo, zǒu ba!|D’accord, allons-y !'''),
'Distingue qù / qí, l’articulation du g de gōnggòng et les tons de Běijīng.',
'Décris ton lieu d’étude, les matières, la fréquence des révisions et le trajet jusqu’à l’école.')

add(13,'你喜欢中餐还是西餐','Préfères-tu la cuisine chinoise ou occidentale ?','Do you like Chinese food or Western food',121,
'Exprimer des goûts, choisir entre deux options avec 还是, proposer un repas et commander.',
'''喜欢|xǐhuan|aimer / apprécier
中餐|zhōngcān|cuisine chinoise
西餐|xīcān|cuisine occidentale
还是|háishi|ou (dans une question)
或者|huòzhě|ou (dans une affirmation)
吃|chī|manger
喝|hē|boire
米饭|mǐfàn|riz cuit
面条|miàntiáo|nouilles
饺子|jiǎozi|ravioli chinois
包子|bāozi|brioche farcie
菜|cài|plat / légume
肉|ròu|viande
鸡肉|jīròu|poulet
鱼|yú|poisson
牛肉|niúròu|bœuf
茶|chá|thé
咖啡|kāfēi|café
好吃|hǎochī|délicieux
好喝|hǎohē|bon à boire
辣|là|piquant
甜|tián|sucré
清淡|qīngdàn|léger (nourriture)
点菜|diǎn cài|commander un plat
菜单|càidān|menu''',
'''Choix interrogatif 还是|Dans une question qui propose des alternatives, on emploie 还是.|你喜欢茶还是咖啡？|Nǐ xǐhuan chá háishi kāfēi?|Tu préfères le thé ou le café ?
Alternative déclarative 或者|Dans un énoncé affirmatif, on utilise souvent 或者 pour « ou ».|我喝茶或者水。|Wǒ hē chá huòzhě shuǐ.|Je bois du thé ou de l’eau.
Goûts avec 喜欢|喜欢 est placé avant un nom ou un verbe qui représente l’activité aimée.|我喜欢吃面条。|Wǒ xǐhuan chī miàntiáo.|J’aime manger des nouilles.''',
('Choisir un restaurant','Deux amis décident où déjeuner.','''A|你喜欢中餐还是西餐？|Nǐ xǐhuan zhōngcān háishi xīcān?|Tu préfères la cuisine chinoise ou occidentale ?
B|我喜欢中餐。|Wǒ xǐhuan zhōngcān.|Je préfère la cuisine chinoise.
A|你喜欢吃辣的吗？|Nǐ xǐhuan chī là de ma?|Tu aimes la nourriture épicée ?
B|不太喜欢，我喜欢清淡的菜。|Bú tài xǐhuan, wǒ xǐhuan qīngdàn de cài.|Pas beaucoup, je préfère les plats légers.
A|那我们去吃饺子吧。|Nà wǒmen qù chī jiǎozi ba.|Alors allons manger des raviolis.
B|好啊，我很喜欢饺子！|Hǎo a, wǒ hěn xǐhuan jiǎozi!|Oui, j’adore ça !'''),
('Au restaurant','Une serveuse prend la commande.','''A|您好，请问要点菜吗？|Nín hǎo, qǐngwèn yào diǎn cài ma?|Bonjour, souhaitez-vous commander ?
B|要，一份米饭和一份鱼。|Yào, yí fèn mǐfàn hé yí fèn yú.|Oui, du riz et du poisson.
A|您喝茶还是咖啡？|Nín hē chá háishi kāfēi?|Thé ou café ?
B|我要一杯茶。|Wǒ yào yì bēi chá.|Une tasse de thé.
A|好的，请稍等。|Hǎo de, qǐng shāo děng.|Très bien, un instant.
B|谢谢！|Xièxie!|Merci !'''),
'Exerce sh / x dans xǐhuan, xīcān, et le ton 4 de là.',
'Demande les goûts de ton partenaire : plats, boissons et niveau de piquant ; passe une commande.')

add(14,'我搬家了','J’ai déménagé','I’ve moved',134,
'Parler d’un déménagement, d’une nouvelle situation, de lieux et des changements introduits par 了.',
'''搬家|bānjiā|déménager
了|le|particule d’accompli / changement
新|xīn|nouveau
旧|jiù|ancien
房子|fángzi|maison / appartement
公寓|gōngyù|appartement
房间|fángjiān|chambre
地址|dìzhǐ|adresse
附近|fùjìn|alentours
漂亮|piàoliang|joli
安静|ānjìng|calme
热闹|rènao|animé
方便|fāngbiàn|pratique
离|lí|être éloigné de
近|jìn|près
远|yuǎn|loin
找到|zhǎodào|trouver
钥匙|yàoshi|clé
沙发|shāfā|canapé
家具|jiājù|meubles
帮忙|bāngmáng|donner un coup de main
整理|zhěnglǐ|ranger
干净|gānjìng|propre
累|lèi|fatigué
已经|yǐjīng|déjà''',
'''Changement avec 了|En fin de phrase, 了 peut marquer une nouvelle situation, par exemple déménager.|我搬家了。|Wǒ bānjiā le.|J’ai déménagé.
Distance avec 离|A 离 B 近 / 远 donne la distance relative entre deux lieux.|我家离学校很近。|Wǒ jiā lí xuéxiào hěn jìn.|J’habite près de l’école.
Résultat avec 到|到 placé après un verbe peut marquer l’atteinte d’un résultat.|我找到新房子了。|Wǒ zhǎodào xīn fángzi le.|J’ai trouvé un nouvel appartement.''',
('Annoncer son déménagement','Une amie appelle après avoir changé d’adresse.','''A|听说你搬家了？|Tīngshuō nǐ bānjiā le?|J’ai entendu dire que tu as déménagé ?
B|对，我搬到新公寓了。|Duì, wǒ bān dào xīn gōngyù le.|Oui, dans un nouvel appartement.
A|新房子怎么样？|Xīn fángzi zěnmeyàng?|Il est comment ?
B|很漂亮，也很安静。|Hěn piàoliang, yě hěn ānjìng.|Très joli et calme.
A|离学校远吗？|Lí xuéxiào yuǎn ma?|C’est loin de l’école ?
B|不远，走路十分钟。|Bù yuǎn, zǒulù shí fēnzhōng.|Non, dix minutes à pied.'''),
('Aider à emménager','Un ami arrive avec des cartons.','''A|你需要帮忙吗？|Nǐ xūyào bāngmáng ma?|As-tu besoin d’aide ?
B|需要，谢谢你！|Xūyào, xièxie nǐ!|Oui, merci !
A|这些书放在哪儿？|Zhèxiē shū fàng zài nǎr?|Où dois-je mettre ces livres ?
B|放在桌子上吧。|Fàng zài zhuōzi shang ba.|Sur la table, s’il te plaît.
A|我们整理完了吗？|Wǒmen zhěnglǐ wán le ma?|On a fini de ranger ?
B|还没有，沙发还没搬。|Hái méiyǒu, shāfā hái méi bān.|Pas encore, il reste le canapé.'''),
'Répète bān / bàn, jìn / jìng et la particule le qui se prononce légère.',
'Annonce une nouvelle adresse, décris le quartier et demande une aide pour emménager.')

add(15,'周末我们去了天津','Nous sommes allés à Tianjin le week-end','We went to Tianjin at the weekend',146,
'Raconter une sortie passée, situer les actions achevées et les séquences avec 了 et 先…然后.',
'''周末|zhōumò|week-end
上周|shàng zhōu|semaine dernière
昨天|zuótiān|hier
去年|qùnián|année dernière
天津|Tiānjīn|Tianjin
旅游|lǚyóu|voyager
旅行|lǚxíng|voyage
去|qù|aller
去了|qù le|est allé
坐火车|zuò huǒchē|prendre le train
坐飞机|zuò fēijī|prendre l’avion
火车站|huǒchēzhàn|gare
参观|cānguān|visiter
拍照|pāizhào|prendre des photos
景点|jǐngdiǎn|site touristique
博物馆|bówùguǎn|musée
有意思|yǒu yìsi|intéressant
好玩|hǎowán|amusant
先|xiān|d’abord
然后|ránhòu|ensuite
最后|zuìhòu|enfin
回来|huílái|revenir
买票|mǎi piào|acheter des billets
玩|wán|s’amuser
天气|tiānqì|temps (météo)''',
'''Accompli avec 了|Après le verbe, 了 indique souvent qu’une action a été réalisée.|我们去了天津。|Wǒmen qù le Tiānjīn.|Nous sommes allés à Tianjin.
Raconter en ordre|先…然后…最后… décrit la succession des étapes d’une activité.|我们先参观，然后吃饭。|Wǒmen xiān cānguān, ránhòu chīfàn.|Nous avons d’abord visité, puis mangé.
Interroger le passé|Le marqueur 了 peut apparaître dans une question sur un événement achevé.|你昨天去哪儿了？|Nǐ zuótiān qù nǎr le?|Où es-tu allé hier ?''',
('Retour d’excursion','Deux étudiants se racontent leur week-end.','''A|周末你去哪儿了？|Zhōumò nǐ qù nǎr le?|Où es-tu allé ce week-end ?
B|我跟朋友去了天津。|Wǒ gēn péngyou qù le Tiānjīn.|Je suis allé à Tianjin avec des amis.
A|你们坐火车去的吗？|Nǐmen zuò huǒchē qù de ma?|Vous avez pris le train ?
B|对，我们坐火车去的。|Duì, wǒmen zuò huǒchē qù de.|Oui, nous avons pris le train.
A|好玩吗？|Hǎowán ma?|C’était amusant ?
B|非常好玩！|Fēicháng hǎowán!|Très amusant !'''),
('Montrer des photos','Au retour de voyage.','''A|这些照片是在哪儿拍的？|Zhèxiē zhàopiàn shì zài nǎr pāi de?|Où as-tu pris ces photos ?
B|在天津的博物馆。|Zài Tiānjīn de bówùguǎn.|Au musée de Tianjin.
A|你们先做了什么？|Nǐmen xiān zuò le shénme?|Qu’avez-vous fait d’abord ?
B|我们先参观博物馆。|Wǒmen xiān cānguān bówùguǎn.|Nous avons d’abord visité le musée.
A|然后呢？|Ránhòu ne?|Et ensuite ?
B|然后吃了晚饭，最后回北京。|Ránhòu chī le wǎnfàn, zuìhòu huí Běijīng.|Puis nous avons dîné, enfin nous sommes rentrés à Pékin.'''),
'Répète lǚyóu, huǒchē, zhàopiàn et différencie qù / qǔ.',
'Raconte ta dernière sortie en six phrases avec un lieu, un transport et trois étapes chronologiques.')

add(16,'你能教英语吗','Peux-tu enseigner l’anglais ?','Can you teach English',158,
'Demander une capacité, solliciter une aide, distinguer 会, 能 et 可以, inviter à enseigner.',
'''能|néng|pouvoir (capacité, possibilité)
会|huì|savoir faire (appris)
可以|kěyǐ|pouvoir / être autorisé
教|jiāo|enseigner
英语|Yīngyǔ|anglais
汉语|Hànyǔ|chinois
说|shuō|parler
写|xiě|écrire
读|dú|lire
听|tīng|écouter
电脑|diànnǎo|ordinateur
打字|dǎzì|taper au clavier
帮忙|bāngmáng|aider
问题|wèntí|question / problème
明白|míngbai|comprendre
懂|dǒng|comprendre
解释|jiěshì|expliquer
慢|màn|lent
快|kuài|rapide
再|zài|de nouveau
一遍|yí biàn|une fois / un passage
发音|fāyīn|prononciation
练习|liànxí|pratique
一起|yìqǐ|ensemble''',
'''Capacité apprise 会|会 indique souvent un savoir-faire acquis, comme parler une langue.|我会说英语。|Wǒ huì shuō Yīngyǔ.|Je sais parler anglais.
Possibilité / capacité 能|能 peut exprimer les circonstances et la capacité à accomplir une action.|你今天能来吗？|Nǐ jīntiān néng lái ma?|Peux-tu venir aujourd’hui ?
Permission 可以|可以 est courant pour demander ou accorder une permission.|我可以问一个问题吗？|Wǒ kěyǐ wèn yí ge wèntí ma?|Puis-je poser une question ?''',
('Entraide linguistique','Deux étudiants échangent leurs compétences.','''A|你会说英语吗？|Nǐ huì shuō Yīngyǔ ma?|Sais-tu parler anglais ?
B|会一点儿。|Huì yìdiǎnr.|Un peu.
A|你能教我英语吗？|Nǐ néng jiāo wǒ Yīngyǔ ma?|Peux-tu m’enseigner l’anglais ?
B|当然可以。|Dāngrán kěyǐ.|Bien sûr.
A|我也可以教你汉语。|Wǒ yě kěyǐ jiāo nǐ Hànyǔ.|Je peux aussi t’enseigner le chinois.
B|太好了，我们一起学习！|Tài hǎo le, wǒmen yìqǐ xuéxí!|Génial, étudions ensemble !'''),
('En classe','Un apprenant demande une explication.','''A|老师，我可以问一个问题吗？|Lǎoshī, wǒ kěyǐ wèn yí ge wèntí ma?|Professeur, puis-je poser une question ?
B|可以，请说。|Kěyǐ, qǐng shuō.|Oui, vas-y.
A|这个词是什么意思？|Zhège cí shì shénme yìsi?|Que signifie ce mot ?
B|我给你解释一下。|Wǒ gěi nǐ jiěshì yíxià.|Je vais te l’expliquer.
A|请再说一遍，好吗？|Qǐng zài shuō yí biàn, hǎo ma?|Pourriez-vous le répéter ?
B|当然，我说慢一点儿。|Dāngrán, wǒ shuō màn yìdiǎnr.|Bien sûr, je vais parler plus lentement.'''),
'Différencie néng / nèng et les finales -eng et -en ; pratique les tons de kěyǐ.',
'Demande à un partenaire ce qu’il sait faire, ce qu’il peut faire aujourd’hui et une permission.')

add(17,'圣诞节快到了','Noël approche','Christmas is coming',169,
'Parler d’un événement imminent, organiser une fête, inviter, exprimer préparatifs et souhaits.',
'''圣诞节|Shèngdànjié|Noël
春节|Chūnjié|Nouvel An chinois
节日|jiérì|fête
快|kuài|bientôt / rapidement
快要|kuài yào|être sur le point de
到了|dào le|arriver / approcher
准备|zhǔnbèi|préparer
礼物|lǐwù|cadeau
送|sòng|offrir / envoyer
收到|shōudào|recevoir
庆祝|qìngzhù|célébrer
聚会|jùhuì|réunion / fête
邀请|yāoqǐng|inviter
参加|cānjiā|participer
一起|yìqǐ|ensemble
唱歌|chànggē|chanter
跳舞|tiàowǔ|danser
蛋糕|dàngāo|gâteau
开心|kāixīn|heureux
快乐|kuàilè|joyeux
希望|xīwàng|espérer
打算|dǎsuàn|prévoir
还有|hái yǒu|il reste / encore
明年|míngnián|l’an prochain''',
'''Événement imminent 快…了|快 + verbe / adjectif + 了 indique qu’un changement va bientôt arriver.|圣诞节快到了。|Shèngdànjié kuài dào le.|Noël approche.
Projet avec 打算|打算 annonce une intention ou un programme prévu.|我打算买礼物。|Wǒ dǎsuàn mǎi lǐwù.|Je compte acheter des cadeaux.
Invitation|邀请 + personne + activité / événement sert à convier quelqu’un.|我想邀请你参加聚会。|Wǒ xiǎng yāoqǐng nǐ cānjiā jùhuì.|Je veux t’inviter à la fête.''',
('Inviter à la fête','Une étudiante organise Noël.','''A|圣诞节快到了！|Shèngdànjié kuài dào le!|Noël approche !
B|对，你有什么打算？|Duì, nǐ yǒu shénme dǎsuàn?|Oui, quels sont tes projets ?
A|我想举行一个聚会。|Wǒ xiǎng jǔxíng yí ge jùhuì.|Je voudrais organiser une fête.
B|太好了！我可以来吗？|Tài hǎo le! Wǒ kěyǐ lái ma?|Super ! Je peux venir ?
A|当然，我想邀请你。|Dāngrán, wǒ xiǎng yāoqǐng nǐ.|Bien sûr, je voulais t’inviter.
B|谢谢，我一定来！|Xièxie, wǒ yídìng lái!|Merci, je viendrai !'''),
('Préparer des cadeaux','Deux amis font leurs courses.','''A|你准备好礼物了吗？|Nǐ zhǔnbèi hǎo lǐwù le ma?|As-tu préparé les cadeaux ?
B|还没有，我明天去买。|Hái méiyǒu, wǒ míngtiān qù mǎi.|Pas encore, j’irai demain.
A|你要送给谁？|Nǐ yào sòng gěi shéi?|À qui veux-tu les offrir ?
B|送给我的朋友。|Sòng gěi wǒ de péngyou.|À mes amis.
A|我们一起去吧！|Wǒmen yìqǐ qù ba!|Allons-y ensemble !
B|好，圣诞快乐！|Hǎo, Shèngdàn kuàilè!|D’accord, joyeux Noël !'''),
'Entraîne-toi sur jié, jiè, chàng, qìng et les syllabes de Shèngdànjié.',
'Prépare une invitation comprenant date, lieu, activités et cadeaux ; réponds à une invitation.')

add(18,'我们每天打一个多小时乒乓球','Nous jouons au ping-pong plus d’une heure chaque jour','We play pingpong for over an hour every day',181,
'Parler des loisirs, des durées, des fréquences et des compléments de durée.',
'''每天|měitiān|chaque jour
打|dǎ|jouer (sport de balle)
乒乓球|pīngpāngqiú|ping-pong
篮球|lánqiú|basket-ball
足球|zúqiú|football
羽毛球|yǔmáoqiú|badminton
游泳|yóuyǒng|nager
跑步|pǎobù|courir
锻炼|duànliàn|s’entraîner physiquement
小时|xiǎoshí|heure (durée)
分钟|fēnzhōng|minute
一个多小时|yí ge duō xiǎoshí|plus d’une heure
多|duō|plus de / davantage
次|cì|fois
每周|měi zhōu|chaque semaine
多久|duōjiǔ|combien de temps
多长时间|duō cháng shíjiān|combien de temps
经常|jīngcháng|souvent
运动|yùndòng|sport / faire du sport
身体|shēntǐ|corps / santé
健康|jiànkāng|en bonne santé
累|lèi|fatigué
坚持|jiānchí|persévérer
一起|yìqǐ|ensemble''',
'''Durée après le verbe|La durée d’une activité vient souvent après le verbe et son complément éventuel selon le schéma choisi.|我们打一个小时乒乓球。|Wǒmen dǎ yí ge xiǎoshí pīngpāngqiú.|Nous jouons au ping-pong pendant une heure.
Quantité approximative avec 多|多 après une unité de quantité peut indiquer une durée un peu supérieure.|我跑了一个多小时。|Wǒ pǎo le yí ge duō xiǎoshí.|J’ai couru pendant plus d’une heure.
Fréquence avec 次|次 est le classificateur du nombre de fois qu’une action est accomplie.|我每周游泳两次。|Wǒ měi zhōu yóuyǒng liǎng cì.|Je nage deux fois par semaine.''',
('Routine sportive','Deux camarades parlent de sport.','''A|你喜欢什么运动？|Nǐ xǐhuan shénme yùndòng?|Quel sport aimes-tu ?
B|我喜欢打乒乓球。|Wǒ xǐhuan dǎ pīngpāngqiú.|J’aime le ping-pong.
A|你每天打多久？|Nǐ měitiān dǎ duōjiǔ?|Tu joues combien de temps par jour ?
B|一个多小时。|Yí ge duō xiǎoshí.|Plus d’une heure.
A|你不累吗？|Nǐ bú lèi ma?|Tu n’es pas fatigué ?
B|有点儿累，但是很开心。|Yǒudiǎnr lèi, dànshì hěn kāixīn.|Un peu, mais je suis content.'''),
('Faire du sport ensemble','Au gymnase.','''A|你每周运动几次？|Nǐ měi zhōu yùndòng jǐ cì?|Combien de fois fais-tu du sport par semaine ?
B|三次。你呢？|Sān cì. Nǐ ne?|Trois fois. Et toi ?
A|我每周游泳两次。|Wǒ měi zhōu yóuyǒng liǎng cì.|Je nage deux fois par semaine.
B|明天一起打球吧！|Míngtiān yìqǐ dǎ qiú ba!|Jouons ensemble demain !
A|好，下午四点见。|Hǎo, xiàwǔ sì diǎn jiàn.|D’accord, à quatre heures.
B|太好了！|Tài hǎo le!|Super !'''),
'Répète le rythme de pīngpāngqiú, duōjiǔ, yùndòng et différencie cì / zì.',
'Décris trois loisirs et précise, pour chacun, sa fréquence et sa durée habituelle.')

add(19,'电脑已经修好了','L’ordinateur est réparé','The computer is fixed',193,
'Décrire un problème matériel, un résultat d’action avec 好 / 完 et un changement achevé.',
'''电脑|diànnǎo|ordinateur
手机|shǒujī|téléphone portable
坏|huài|cassé / en panne
修|xiū|réparer
修好|xiūhǎo|réparer avec succès
已经|yǐjīng|déjà
还没|hái méi|pas encore
了|le|particule d’accompli
好|hǎo|bien / terminé
完|wán|finir
做完|zuòwán|terminer de faire
找到|zhǎodào|trouver
作业|zuòyè|devoirs
文件|wénjiàn|fichier
保存|bǎocún|enregistrer
开机|kāijī|allumer (ordinateur)
关机|guānjī|éteindre (ordinateur)
网络|wǎngluò|réseau / Internet
上网|shàngwǎng|aller sur Internet
需要|xūyào|avoir besoin
问题|wèntí|problème
师傅|shīfu|technicien / artisan
重新|chóngxīn|à nouveau
终于|zhōngyú|enfin''',
'''Résultat 好|Le complément 好 peut indiquer qu’une action a réussi ou est achevée de manière satisfaisante.|电脑修好了。|Diànnǎo xiūhǎo le.|L’ordinateur est réparé.
Résultat 完|完 marque l’achèvement complet de l’action.|我做完作业了。|Wǒ zuòwán zuòyè le.|J’ai terminé les devoirs.
Déjà et pas encore|已经…了 décrit une action réalisée ; 还没… marque sa non-réalisation.|我已经找到文件了。|Wǒ yǐjīng zhǎodào wénjiàn le.|J’ai déjà retrouvé le fichier.''',
('Panne d’ordinateur','Deux amis parlent d’un dépannage.','''A|你的电脑怎么了？|Nǐ de diànnǎo zěnme le?|Qu’a ton ordinateur ?
B|昨天坏了，不能开机。|Zuótiān huài le, bù néng kāijī.|Il est tombé en panne hier, impossible de l’allumer.
A|现在修好了吗？|Xiànzài xiūhǎo le ma?|Est-il réparé maintenant ?
B|已经修好了。|Yǐjīng xiūhǎo le.|Oui, c’est déjà réparé.
A|太好了！文件都在吗？|Tài hǎo le! Wénjiàn dōu zài ma?|Super ! Tes fichiers sont toujours là ?
B|都在，谢谢关心。|Dōu zài, xièxie guānxīn.|Oui, tous, merci de t’en soucier.'''),
('Terminer les devoirs','Une étudiante doit envoyer un fichier.','''A|你做完作业了吗？|Nǐ zuòwán zuòyè le ma?|Tu as terminé les devoirs ?
B|还没做完。|Hái méi zuòwán.|Pas encore.
A|你的电脑有问题吗？|Nǐ de diànnǎo yǒu wèntí ma?|Ton ordinateur a un problème ?
B|网络坏了，不能上网。|Wǎngluò huài le, bù néng shàngwǎng.|Internet est en panne.
A|你可以用我的电脑。|Nǐ kěyǐ yòng wǒ de diànnǎo.|Tu peux utiliser mon ordinateur.
B|谢谢，我马上完成。|Xièxie, wǒ mǎshàng wánchéng.|Merci, je vais finir tout de suite.'''),
'Pratique les tons de xiūhǎo, zuòwán et yǐjīng ; distingue jiàn / jiā.',
'Décris une panne, explique les étapes de réparation et dis si le problème est déjà résolu.')

add(20,'把照片贴在墙上','Colle les photos au mur','Stick the photographs on the wall',204,
'Donner des consignes d’aménagement, introduire 把, les compléments de lieu et les verbes de placement.',
'''把|bǎ|marqueur d’objet déplacé / affecté
照片|zhàopiàn|photographie
贴|tiē|coller / afficher
墙|qiáng|mur
墙上|qiáng shang|sur le mur
桌子|zhuōzi|table
桌上|zhuō shang|sur la table
地上|dì shang|par terre
放|fàng|mettre / poser
拿|ná|prendre
挂|guà|suspendre
搬|bān|déplacer (objet lourd)
整理|zhěnglǐ|ranger
干净|gānjìng|propre
漂亮|piàoliang|joli
房间|fángjiān|chambre
柜子|guìzi|armoire
椅子|yǐzi|chaise
书|shū|livre
本|běn|classificateur des livres
张|zhāng|classificateur des objets plats
幅|fú|classificateur d’image / tableau
左边|zuǒbian|côté gauche
右边|yòubian|côté droit''',
'''Structure 把|Avec 把, on place l’objet concerné avant le verbe pour préciser ce qu’on lui fait.|把照片贴在墙上。|Bǎ zhàopiàn tiē zài qiáng shang.|Colle la photo au mur.
Destination avec 在|Après un verbe de placement, 在 + lieu indique où l’objet se retrouve.|把书放在桌子上。|Bǎ shū fàng zài zhuōzi shang.|Pose le livre sur la table.
Mesures 张 / 本|On emploie 张 pour une photo et 本 pour un livre.|把两张照片放好。|Bǎ liǎng zhāng zhàopiàn fàng hǎo.|Range bien les deux photos.''',
('Décorer sa chambre','Deux colocataires préparent leur décoration.','''A|我们把照片贴在哪儿？|Wǒmen bǎ zhàopiàn tiē zài nǎr?|Où colle-t-on les photos ?
B|把照片贴在墙上吧。|Bǎ zhàopiàn tiē zài qiáng shang ba.|Collons-les au mur.
A|这张照片放左边吗？|Zhè zhāng zhàopiàn fàng zuǒbian ma?|Cette photo va à gauche ?
B|对，那张放右边。|Duì, nà zhāng fàng yòubian.|Oui, l’autre à droite.
A|现在房间更漂亮了！|Xiànzài fángjiān gèng piàoliang le!|La pièce est encore plus jolie !
B|我也这么觉得。|Wǒ yě zhème juéde.|Moi aussi, je trouve.'''),
('Ranger le bureau','Instructions entre camarades.','''A|请把书放在桌子上。|Qǐng bǎ shū fàng zài zhuōzi shang.|Mets les livres sur le bureau, s’il te plaît.
B|好的，这些书放哪儿？|Hǎo de, zhèxiē shū fàng nǎr?|D’accord, où vont ces livres ?
A|把它们放在柜子里。|Bǎ tāmen fàng zài guìzi li.|Mets-les dans l’armoire.
B|椅子呢？|Yǐzi ne?|Et la chaise ?
A|把椅子搬到窗户旁边。|Bǎ yǐzi bān dào chuānghu pángbiān.|Déplace-la près de la fenêtre.
B|好了，都整理好了！|Hǎo le, dōu zhěnglǐ hǎo le!|Voilà, tout est rangé !'''),
'Distingue bǎ / bà, zhāng / zhàng et le ton de qiáng.',
'Donne cinq instructions de rangement utilisant 把 avec objets et destinations précises.')

add(21,'明天最高气温10度','Demain, la température maximale sera de 10 degrés','The highest temperature tomorrow will be 10 degrees',215,
'Dire la météo, les températures, comparer des périodes et préparer des vêtements adaptés.',
'''天气|tiānqì|météo / temps
气温|qìwēn|température de l’air
温度|wēndù|température
最高|zuìgāo|le plus élevé
最低|zuìdī|le plus bas
度|dù|degré
零下|língxià|au-dessous de zéro
明天|míngtiān|demain
今天|jīntiān|aujourd’hui
昨天|zuótiān|hier
晴天|qíngtiān|ciel dégagé
阴天|yīntiān|ciel couvert
多云|duōyún|nuageux
下雨|xiàyǔ|pleuvoir
下雪|xiàxuě|neiger
刮风|guāfēng|venter
冷|lěng|froid
热|rè|chaud
凉快|liángkuai|frais / agréable
暖和|nuǎnhuo|doux / chaud
预报|yùbào|prévision
带|dài|emporter
雨伞|yǔsǎn|parapluie
外套|wàitào|manteau / veste
比|bǐ|comparatif (« que »)''',
'''Superlatif avec 最|最 placé devant un adjectif indique le plus haut degré dans un contexte.|今天最高气温十度。|Jīntiān zuìgāo qìwēn shí dù.|Aujourd’hui, la température maximale est de 10 degrés.
Comparaison avec 比|A 比 B + adjectif permet de comparer deux entités.|明天比今天冷。|Míngtiān bǐ jīntiān lěng.|Demain, il fera plus froid qu’aujourd’hui.
Météo avec 下|下雨 et 下雪 sont des expressions verbales pour la pluie et la neige.|明天可能下雪。|Míngtiān kěnéng xiàxuě.|Il pourrait neiger demain.''',
('Consulter la météo','Avant de sortir.','''A|明天天气怎么样？|Míngtiān tiānqì zěnmeyàng?|Quel temps fera-t-il demain ?
B|天气预报说会下雨。|Tiānqì yùbào shuō huì xiàyǔ.|La météo annonce de la pluie.
A|最高气温多少度？|Zuìgāo qìwēn duōshao dù?|Quelle sera la température maximale ?
B|十度，最低三度。|Shí dù, zuìdī sān dù.|10 degrés, minimum 3.
A|那我得带外套。|Nà wǒ děi dài wàitào.|Alors je dois prendre une veste.
B|别忘了带雨伞！|Bié wàng le dài yǔsǎn!|N’oublie pas le parapluie !'''),
('Comparer les saisons','Deux personnes parlent du temps.','''A|今天比昨天冷吗？|Jīntiān bǐ zuótiān lěng ma?|Fait-il plus froid qu’hier ?
B|对，今天冷多了。|Duì, jīntiān lěng duō le.|Oui, beaucoup plus froid.
A|冬天常常下雪吗？|Dōngtiān chángcháng xiàxuě ma?|Neige-t-il souvent en hiver ?
B|在这里不常下雪。|Zài zhèlǐ bù cháng xiàxuě.|Pas souvent ici.
A|你喜欢什么天气？|Nǐ xǐhuan shénme tiānqì?|Quel temps préfères-tu ?
B|我喜欢晴天。|Wǒ xǐhuan qíngtiān.|Je préfère le soleil.'''),
'Répète les tons de qìwēn, wēndù, yǔsǎn et l’enchaînement de zuìgāo.',
'Présente une prévision pour demain (soleil / pluie, minimum et maximum) et conseille une tenue.')

add(22,'我正在看新闻','Je regarde les informations en ce moment','I’m watching the news',227,
'Parler d’une action en cours avec 正在, des médias, de ce que les gens font au même moment.',
'''正在|zhèngzài|être en train de
在|zài|en cours de / à
看|kàn|regarder / lire
新闻|xīnwén|actualités
电视|diànshì|télévision
电影|diànyǐng|film
节目|jiémù|émission
听|tīng|écouter
音乐|yīnyuè|musique
广播|guǎngbō|radio
手机|shǒujī|portable
打电话|dǎ diànhuà|téléphoner
发消息|fā xiāoxi|envoyer un message
上网|shàngwǎng|surfer sur Internet
做饭|zuòfàn|cuisiner
做作业|zuò zuòyè|faire ses devoirs
学习|xuéxí|étudier
睡觉|shuìjiào|dormir
现在|xiànzài|maintenant
呢|ne|particule de progression / relance
别|bié|ne… pas (interdiction)
打扰|dǎrǎo|déranger
等|děng|attendre
马上|mǎshàng|tout de suite''',
'''Progressif avec 正在|正在 devant le verbe souligne l’action actuellement en cours.|我正在看新闻。|Wǒ zhèngzài kàn xīnwén.|Je regarde les informations.
Progressif avec 在…呢|在 + verbe + 呢 peut insister sur une action en cours.|他在做作业呢。|Tā zài zuò zuòyè ne.|Il est en train de faire ses devoirs.
Interdiction avec 别|别 placé devant le verbe permet de demander de ne pas faire quelque chose.|别打扰他。|Bié dǎrǎo tā.|Ne le dérange pas.''',
('Que fais-tu ?','Un appel pendant les informations.','''A|喂，你在做什么？|Wéi, nǐ zài zuò shénme?|Allô, que fais-tu ?
B|我正在看新闻呢。|Wǒ zhèngzài kàn xīnwén ne.|Je regarde les informations.
A|今天有什么新闻？|Jīntiān yǒu shénme xīnwén?|Quelles sont les nouvelles ?
B|我正在看天气预报。|Wǒ zhèngzài kàn tiānqì yùbào.|Je regarde les prévisions météo.
A|那我等一会儿再打电话。|Nà wǒ děng yíhuìr zài dǎ diànhuà.|Je rappellerai un peu plus tard.
B|好的，一会儿见。|Hǎo de, yíhuìr jiàn.|D’accord, à tout à l’heure.'''),
('À la maison','Parler des activités de chacun.','''A|妈妈在做什么？|Māma zài zuò shénme?|Que fait maman ?
B|她正在做饭。|Tā zhèngzài zuòfàn.|Elle cuisine.
A|爸爸呢？|Bàba ne?|Et papa ?
B|他在听音乐呢。|Tā zài tīng yīnyuè ne.|Il écoute de la musique.
A|弟弟在睡觉吗？|Dìdi zài shuìjiào ma?|Mon petit frère dort ?
B|不，他在写作业。|Bù, tā zài xiě zuòyè.|Non, il fait ses devoirs.'''),
'Entraîne-toi sur zhèngzài, xīnwén, diànyǐng et les finales -ing / -in.',
'Décris cinq actions en cours à la maison, dans la rue ou dans la classe.')

add(23,'时间过得真快','Comme le temps passe vite !','Time flies',238,
'Faire un bilan du temps passé, évoquer l’expérience et les projets, exprimer la vitesse ou la durée d’un changement.',
'''时间|shíjiān|temps
过|guò|passer / expérience
得|de|particule de complément
真|zhēn|vraiment
快|kuài|vite
慢|màn|lentement
已经|yǐjīng|déjà
一年|yì nián|un an
半年|bàn nián|six mois
以前|yǐqián|avant
以后|yǐhòu|après / plus tard
现在|xiànzài|maintenant
将来|jiānglái|avenir
毕业|bìyè|obtenir son diplôme
学习|xuéxí|étudier
汉语|Hànyǔ|chinois
进步|jìnbù|faire des progrès
提高|tígāo|améliorer
水平|shuǐpíng|niveau
希望|xīwàng|espérer
计划|jìhuà|projet / planifier
记得|jìde|se rappeler
忘记|wàngjì|oublier
努力|nǔlì|faire des efforts
继续|jìxù|continuer
见面|jiànmiàn|se retrouver''',
'''Complément de degré 得|Le schéma verbe + 得 + adjectif décrit la manière ou le degré du déroulement.|时间过得真快！|Shíjiān guò de zhēn kuài!|Comme le temps passe vite !
Expérience avec 过|Après un verbe, 过 peut marquer une expérience vécue au moins une fois.|我去过北京。|Wǒ qù guo Běijīng.|Je suis déjà allé à Pékin.
Avant / après|以前 et 以后 permettent de situer deux périodes dans le temps.|毕业以后我想继续学习。|Bìyè yǐhòu wǒ xiǎng jìxù xuéxí.|Après mon diplôme, je veux continuer à étudier.''',
('Bilan du semestre','Deux étudiants terminent leur cours.','''A|时间过得真快！|Shíjiān guò de zhēn kuài!|Comme le temps passe vite !
B|是啊，我们已经学了半年汉语。|Shì a, wǒmen yǐjīng xué le bàn nián Hànyǔ.|Oui, cela fait six mois que nous étudions le chinois.
A|你觉得自己进步了吗？|Nǐ juéde zìjǐ jìnbù le ma?|Penses-tu avoir progressé ?
B|进步了，但是还要努力。|Jìnbù le, dànshì hái yào nǔlì.|Oui, mais je dois encore travailler.
A|以后你有什么计划？|Yǐhòu nǐ yǒu shénme jìhuà?|Quels sont tes projets ?
B|我想继续学汉语。|Wǒ xiǎng jìxù xué Hànyǔ.|Je veux continuer le chinois.'''),
('Garder le contact','Des camarades vont quitter l’université.','''A|你毕业以后去哪儿？|Nǐ bìyè yǐhòu qù nǎr?|Où iras-tu après ton diplôme ?
B|我打算回国工作。|Wǒ dǎsuàn huíguó gōngzuò.|Je compte travailler dans mon pays.
A|我们以后还能见面吗？|Wǒmen yǐhòu hái néng jiànmiàn ma?|Pourrons-nous nous revoir ?
B|当然！我们保持联系。|Dāngrán! Wǒmen bǎochí liánxì.|Bien sûr ! Restons en contact.
A|祝你一切顺利！|Zhù nǐ yíqiè shùnlì!|Je te souhaite le meilleur !
B|谢谢，你也是！|Xièxie, nǐ yě shì!|Merci, à toi aussi !'''),
'Pratique le ton neutre de de et guo ; contraste guò (passer) et guo (expérience).',
'Réalise une présentation finale de deux minutes : bilan, progrès, expérience, plans et remerciements.')

out=Path(__file__).resolve().parents[1]/'data'/'lessons.json'
assert len(L)==23,len(L)
assert [x['id'] for x in L]==list(range(1,24))
assert all(len(x['dialogs'])==2 and len(x['grammar'])==3 and len(x['vocab'])>=19 for x in L)
out.write_text(json.dumps({'meta':{'title':'Mandarin Parlé — Developing Chinese I','language':'fr','source':'Développement pédagogique original aligné sur les 23 thèmes et le sommaire du PDF fourni (Elementary Speaking Course I, 2nd edition). Le manuel et ses enregistrements officiels ne sont pas reproduits intégralement.','version':'1.0'},'lessons':L},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(L)} leçons, {sum(len(x["vocab"]) for x in L)} mots, {sum(len(y["lines"]) for x in L for y in x["dialogs"])} répliques, {sum(len(x["grammar"]) for x in L)} points de grammaire -> {out}')
