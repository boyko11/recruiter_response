template_file_absolute_path = "C:\\Users\\boyko\\OneDrive\\Desktop\\recruiter_response\\template"
response_file_absolute_path = "C:\\Users\\boyko\\OneDrive\\Desktop\\response.txt"

name = input("Recruiter Name: ")
job = input("Job Title: ")

template_file = open(template_file_absolute_path)
the_template = template_file.read()

filled_out_template = the_template.format(name, job)


f = open(response_file_absolute_path, 'w+')
f.write(filled_out_template)
f.close()
print("Done")
