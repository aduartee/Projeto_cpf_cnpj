from cpf_cnj import Documento


exemplo_cnpj = "03532920000149"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

exemplo_cpf = "62906403210"
documento2 = Documento.cria_documento(exemplo_cpf)
print(documento2)







