from pydub import AudioSegment
def transform_code(codefile="testcode.txt"):
	replace_obj = ["~","!","@","#","$","%","^","&","*","(",")","{","}","<",">","?",'"',":","|","_","+"]
	replace_tar = ["`","1","2","3","4","5","6","7","8","9","10","[","]",",",".","/","'",";","\\","-","="]
	list_code_obj = []
	list_code_tar = []
	list_code_final = []
	with open(codefile,"r") as f:
		content = f.read()
		content = content.replace("\n","")
		content = content.replace(" ","")
		for each in range(len(replace_obj)):
			content = content.replace(replace_obj[each],replace_tar[each])
		content = content.lower()
		for word in content:
			list_code_obj.append(word)
	with open("codetar.txt","r") as f:
		content = f.read().replace("\n","")
		for target in content:
			list_code_tar.append(target)
	for word in list_code_obj:
		list_code_final.append(list_code_tar.index(word))
	return list_code_final


def audioConcatenate(list_code_final):
	list_music = []
	i = 0
	for each in list_code_final:
		print(i)
		list_music.append(AudioSegment.from_mp3("audio/"+str(each)+".mp3")[300:-300])
		i+=1
	output_music = sum(list_music)
	output_music.export("VGG16.mp3", format="mp3")

list_code_final = transform_code()
audioConcatenate(list_code_final)