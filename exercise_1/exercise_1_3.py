str_1 = 'Data Science Introduction in Python'
str_2 = 'Er hortet Rohre'
str_3 = 'Heute arbeitete er am Computer etwas länger.'

str_1_processed = str_1[2::3]
print(f'str_1_processed: {str_1_processed}')

str_2_processed = str_2[::-1]
print(f'str_2_processed: {str_2_processed}')

str_3_processed = str_3.replace("er", "sie")
print(f'str_3_processed: {str_3_processed}')
