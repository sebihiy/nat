# -*- coding: utf-8 -*-
import random

questions_answers = [
	["Quelle est la devise de la République ?", "Egalité, Liberté, Fraternité"],
	["Peut-on rajouter une 4eme valeur? Selon vous, ce serait laquelle ?", "laÏcité"],
	["C’est quoi la laÏcité ?" , "La laÏcité est regie par 3 principes : liberté de conscience, la separation entre les pouvoirs publics et religieux, et l’égalité devant la loi quelque soit la religion. La France devint laïque en 1905."],
	["Qu’est ce que la democratie ?", "C’est un regime politique où le pouvoir est detenu par le peuple sans qu’il n’y ait de distinctions socio-demographiques ou autres… . Les démocraties peuvent être indirectes quand le pouvoir est exerce par des representants elus lors du suffrage universel."],
	["Etes-vous d’accord avec la democratie ?", "Chacun a son avis !"],
	["Quels sont les droits et les devoirs du citoyen français ?", "Financement des services publics, contribution à la defense nationale, accès aux emplois publics, education …"],
	["Quels sont les symboles de la France ?", "Drapeau, Hymne national, Mariane, Devise de la France, 14 Juillet, Le coq, Le Faisceau de licteur, Le sceau, Fleur de Lys"],
	["Citez des fleuves en France", "Seine, Loire, Garonne, Rhône"],
	["Enumerez des personnages français connus", "– Litterature : Honore de Balzac, Victor Hugo, Albert Camus …\n" + \
							"– Philosophie : Voltaire, Jean- Paul Sartre\n" + \
							"– Peinture : Paul Cezanne, Claude Monet …\n" + \
							"– Musique : Johnny Hallyday, Francis Cabrel, Edith Piaf …\n" + \
							"– Science : D’Alembert, Coulomb, Marie Curie …\n" + \
							"– Sport : Gaël Monfils, Richard Virenque, Zidane, Platini, Yannick Noah …\n" + \
							"– Guerre : Napoleon, Jeanne d’Arc …\n" + \
							"– Architecture : Gustave Eiffel ..\n"],
	["Qui est la Marianne ?", "C’est un des symboles de la France, paysanne au bonnet phrygien qui incarne la Republique et les valeurs de la liberte et de democratie. Elle existe sur les pièces de monnaie. Elle apparaît sur le tableau de Eugène Delacroix."],
	["Quel est l’hymne national de la France ?", "C’est La Marseillaise, qui est à la base un chant patriotique de la Revolution ecrit par Rouget de Lisle en 1792 quand la France a declare la guerre à l’Autriche."],
	["Quelles sont les 3 types de collectivites en France ?", "– Communes : 36 000, – Departements : 101 (96 en France metropolitaine + 5 outre-mer), – Regions : 18"],
	["Pouvez vous citer des departements d’outre mer", "Guadeloupe, Martinique, Guyanne, Reunion, Mayotte"],
	["Dans quel departement habitez-vous? Quel est le nom de votre maire ?", "Alpes-Maritimes, Maire de Antibes, Jean Leonetti"],
	["Donnez des exemples de departements français", "Nord, Cote-d'Or, Charente, Haute-Garonne, Juras, Paris …"],
	["Donnez des noms de grandes villes françaises", "Paris, Toulouse, Lyon, Marseille …"],
	["Quelle est l’emblème de la France et que signifient ses couleurs?", "L’emblème de la France est le drapeau constitue de la couleur rouge, bleue et blanche. Le blanc est la couleur des rois, le bleu est celui de Paris et le rouge fait reference au sang verse pour la liberation du peuple."],
	["Que fête-t-on le 1er mai ?", "La fête du travail, c’est un jour ferie"],
	['Citez 3 monuments historiques', 'Château de Versailles, le Louvres, Châteaux de la Loire …'],
	['Citez des chaînes de montagnes en France', 'Alpes, Pyrenees, Vosges …'],
	['Quel est le point culminant en France ?', 'Le Mont Blanc'],
	['Quels sont les pays frontaliers avec la France ?', 'Allemagne, Belgique, Espagne, Luxembourg, Suisse, Andorre, Monaco, Italie'],
	['Combien de pays comporte l’Union Europeenne ?', '28'],
	['Citez une personne naturalisee', 'Marie Curie'],
	['Donnez le nom de littéraires français et les titres de leurs écrits', '« Baudelaire, Fleurs du mal »; « Emile Zola, L’argent »; « Victor Hugo, les Misérables » …'],
	['Quel est l’âge obligatoire de l’école en France ?', 'De 6 à 16 ans révolus'],
	['Que représente le jour du 11 novembre ? ', 'C’est l’Armistice de 1918, signé le 11 novembre et qui marque la fin de la 1ère guerre mondiale'],
	['Qui est Brigitte Bardot? ', 'C’est une actrice de cinéma, chanteuse et militante pour la cause animale. Personnellement, j’adore son titre « Moi je joue » !'],
	['C’est quoi l’Hôtel de Ville ? ', 'C’est le siège des institutions municipales.'],
	['Qui a écrit « Les Trois Mousquetaires »? ', 'Alexandre Dumas'],
	['Citez un grand événement sportif français ', 'Le Tour de France, une épreuve cycliste'],
	['Citez des plats typiques français ', 'Tartiflette, Coq au Vin, Quiche lorraine, steak tartare …'],
	['A-t-on le droit de porter des signes religieux dans les endroits publics ? ', 'Oui sauf les écoles, les collèges et les lycées publics selon la loi de 2004.'],
	['Quel événement de l’histoire de France vous a-t-il marqué ?', 'Vous pouvez parler de n’importe quel grand événement (Révolution, coupe du monde, déclaration des droits de l’homme …). Il faut juste justifier le choix.'],
	['A quelle date précise a eu la Révolution ?', 'La Révolution a eu lieu en 1789'],
	['Quel événement marquant de la Révolution ? Et dans quel contexte elle a émergé ? ', 'Le 14 Juillet 1789 a marqué la prise de la prison de la Bastille, événement inaugural du début de la Révolution. Elle a eu lieu suite à une crise agricole qui a donné lieu à une grande crise économique et une inflation importante qui se confrontait à des décisions de hausse d’impôts prises par le roi.'],
	['Qui était le roi pendant la Révolution ? ', 'C’était le roi Louis XVI qui a été guillotiné.'],
	['A quoi servait la Bastille avant sa démolition ?', ' Elle servait comme prison d’état dans laquelle a été emprisonné Voltaire, Sade …'],
	['Qui est Jean Moulin ? ', 'Ce fut un haut fonctionnaire et une icône de la résistance française à l’occupant nazi pendant la 2nde guerre mondiale. Il mourut en gare de Metz suite aux tortures et mauvais traitements subis par les Allemands.'],
	['Dans quelle époque ont été bâties les cathédrales gothiques? ', 'Au Moyen-âge'],
	['Quand a eu lieu la Vème République et quel fait marquant ?', 'La constitution de la Vème République a été adoptée en 1958 et a marqué la séparation entre le pouvoir exécutif, législatif et judiciaire.'],
	['Quand a eu lieu la déclaration des droits de l’homme et du citoyen ?', 'Le 26 août 1789'],
	['Donnez-moi les dates des 2 guerres mondiales', '– 1ère guerre : de 1914 au 11 novembre 1918 \n – 2ème guerre : de 1939 au 8 mai 1945'],
	['Dans quelle République sommes-nous ? ', 'C’est la Vème République fondée en 1958 par Charles de Gaulle. Charles de Gaulle était un général et chef de la France Libre. Il s’est réfugié en Angleterre quand l’Allemagne a attaqué la France pendant la 2nde guerre mondiale'],
	['En quelle année fut fondée la 1ère République ? ', 'En 1792'],
	['Comment appelait-on les soldats français pendant la 1ère guerre mondiale ? ', 'Les poilus'],
	['Qui sont les alliés pendant les 2 guerres mondiales ? ', '– 1ère guerre : France, Angleterre, Russie, US \n – 2ème guerre : France, Angleterre, URSS, US'],
	['Donnez le nom de rois français', 'Charlemagne, Clovis, Louis XIV …'],
	['Donnez le nom de reines de France', 'Anne d’Autriche, Marie-Antoinette d’Autriche, Joséphine de la Pagerie, Anne de Bretagne ..'],
	['Citez-moi les présidents de la Vème république dans l’ordre ', 'De Gaulle, Pompidou, Giscard d’Estaing, Mitterand, Chirac, Sarkozy, Hollande, Macron'],
	['Citez-moi des personnes qui ont marqué l’histoire de la France', 'Napoléon, De Gaulle, Charlemagne, Jeanne D’Arc …'],
	['Qui a instauré le code civil en France ? ', 'Napoléon Bonaparte'],
	['Qui a construit le château de Versailles ?', 'Louis XIV'],
	['Qui a construit l’Arc de triomphe', 'Napoléon Ier'],
	['C’est quoi la guerre des 100 ans ?', 'Il s’agit d’un conflit entre les rois de France et de l’Angleterre pendant un siècle pendant le Moyen-Age. Cette guerre a d’ailleurs duré 116 ans plutôt !'],
	['Quelle est la bataille de Verdun ? ', 'Bataille qui s’est déroulée en 1916 entre l’armée française et allemande à Lorraine pendant la 1ère guerre mondiale. Elle a fait bcp de victimes des deux camps et le résultat militaire fut nul'],
	['La Tour Eiffel a été construite pour quel événement ?', 'Pour l’exposition universelle de Paris en 1889'],
	['A quelle année les femmes ont eu le droit de voter en France ?', '1944'],
	['A quel homme politique se rattache la création de l’école publique, gratuite et obligatoire ?', 'Jules Ferry'],
	['Citez 3 pays qui ont fait partie de l’Empire colonial français', 'La Tunisie, l’Algérie, Côte d’Ivoire, Mali, Sénégal …'],
	['En quelle année a eu lieu l’abolition de l’esclavage en France', 'En 1848'],
	['Qui est Voltaire ? Qu’a-t-il écrit? ', 'Voltaire est un écrivain et philosophe français qui a marqué le 18ème siècle appelé Siècle des Lumières. Il a écrit « Traité sur la tolérance » et « Oedipe » …'],
	['Qu’est ce que la philosophie des Lumières?', 'C’est un mouvement philosophique qui a émergé dans le 18ème siècle en Europe où des philosophes européens avaient pour objectif de combattre l’obscurantisme, l’ignorance et diffuser les connaissances'],
	['Citez quelques philosophes français des lumières ', 'Montesquieu, Voltaire, Rousseau, Diderot …'],
	['Quel est le nom du Président actuel et le précédent ?', 'Le président actuel est Emmanuel Macron et le précédent est François Hollande.'],
	['Donnez le nom de quelques ministres actuels ', '– Premier ministre : Edouard Philippe, – Ministre de l’intérieur : Christophe Castaner – Ministre de l’écologie : François de Rugy, – Ministre de l’économie : Bruno Lemair'],
	['Qu’est ce que le pouvoir exécutif ?', 'Le pouvoir exécutif est partagé entre le président de la République (chef de l’État) et le gouvernement dirigé par le Premier ministre. Le rôle du pouvoir exécutif est d’exécuter les lois et décisions de justice. Il dirige la police, la force militaire, l’administration, la diplomatie …'],
	['Pour combien de temps est élu le Président, par quel scrutin et qui a le droit de voter ? ', 'Le Président est élu pour 5 ans au suffrage universel direct, par un scrutin à la majorité absolue à 2 tours. Ceux qui peuvent voter sont les citoyens français majeurs.'],
	['Quel est le siège de la Présidence ? ', 'C’est l’Elysée'],
	['Qu’est ce que le parlement ?', 'Le parlement est composé de 2 chambres : la chambre basse (les députés) et la chambre haute (les sénateurs). Le parlement détient le pouvoir législatif (vote des lois)'],
	['Qu’est ce que l’assemblée nationale ?', 'On l’appelle aussi la chambre basse où siègent les 577 députés de l’Assemblée Nationale. Ils détiennent le pouvoir législatif avec le Sénat.'],
	['Pour combien de temps sont élus les députés et par quel scrutin ?', 'Ils sont élus pour 5 ans au suffrage universel direct uninominal majoritaire à deux tours'],
	['Quel est le siège de l’Assemblée nationale ?', 'Au Palais Bourbon'],
	['Quel est le nom du président actuel de l’Assemblée nationale ?', 'Richard Ferrand'],
	['Qu’est ce que le Sénat ?', 'On l’appelle aussi la chambre haute où siègent les 348 sénateurs, ils détiennent une partie du pouvoir législatif avec les députés.'],
	['Comment sont élus les sénateurs ?', 'Ils sont élus au suffrage universel indirect par 150 000 grands électeurs (maires, conseilleurs généraux…)'],
	['Qui a le pouvoir de diriger la France en cas de décès ou d’incapacité du Président ?', 'C’est le président du sénat.'],
	['Quel est le nom du président actuel du Sénat ? ', 'Gérard Larcher'],
	['Qu’est ce que la cohabitation ?', 'C’est quand le Président est dans l’obligation de nommer un Premier Ministre qui n’appartient pas au même parti politique que lui. La situation s’impose quand la majorité des députés ne sont pas du même parti politique que le Président. Ex : Mitterand/Chirac ou Chirac/Jospin'],
	['Comment devient-on Ministre ou Premier Ministre ?', 'Le Président nomme son premier ministre, le premier ministre définit son gouvernement et le suggère au Président.'],
	['Où sont les bureaux du Premier Ministre ?', 'A l’hotel Matignon.'],
	['Quels sont les 4 premiers personnages de l’état ?', 'Le président, le premier ministre, le président du sénat et enfin le président de l’assemblée nationale'],
	['Comment fonctionnent les élections municipales ?', 'Pour les communes de plus de 1 000 habitants, les conseillers municipaux sont élus au scrutin proportionnel à deux tours'],
	['Donnez le nom d’une personnalité féminine politique ', 'Simone Veil, Ségolène Royal, Martine Aubry …'],
	['Qu’est ce que la loi Veil ?', 'C’est le droit à l’avortement et la contraception pour les femmes qui a été préparée et défendue par Simone Veil ministre de la santé sous la présidence de Valery Giscard d’Estaing'],
	['Quelle personne décide de vous octroyer la nationalité française ? ', 'Ministre de l’intérieur'],
	['Qui gère les relations entre l’état et les institutions religieuses ? ', 'Le ministère du culte, charge du ministre de l’intérieur'],
	['Qui est le chef de l’armée ? ', 'Le Président de la République'],
	['Quelles sont les responsabilites des communes et qui en a la charge ?', 'Elles sont administrées par un maire et un conseil municipal. Elles sont responsables, notamment, des écoles maternelles et primaires, des activités sportives et culturelles, de l’entretien des rues. Elles tiennent l’état civil, c’est-à-dire qu’elles enregistrent les naissances, les mariages, les décès.'],
	['Quelles sont les responsabilites des communes et qui en a la charge ?', 'La France compte 101 départements. Ils sont administrés par les conseils départementaux. Ils sont responsables, notamment, des collèges, de la protection de l’enfance, de l’aide aux personnes âgées.'],
	['Quelles sont les responsabilites des régions et qui en a la charge ?', 'Les régions sont administrées par les conseils régionaux. Elles sont en charge notamment des transports publics, de la formation professionnelle, de la construction et de l’entretien des lycées.'],
	['Qui etait le premier roi francais ?', 'Clovis, en 466'],
	['C’est quoi la dernière loi qui a marqué l’opinion publique?', 'Après l\'Assemblée Nationale(en mars dernier), le Sénat doit adopter ce mardi le projet de loi Santé. Elle prévoit des changements dans notre système actuel de santé notamment : la possibilité au pharmacien de prescrire sous certaine condition des médicaments, un nouvel outil de coordination, ville/hôpital, Les 500 à 600 futurs hôpitaux de proximité labellisés pourront proposer de la chirurgie, etc.']
]

indices = range(0, len(questions_answers))
random.shuffle(indices)

for i in indices:
    print questions_answers[i][0]
    try:
        input("Press enter to see the answer")
    except SyntaxError:
        pass
    print questions_answers[i][1]


