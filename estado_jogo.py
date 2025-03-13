def exibir_estado_jogo(lado_esquerdo, lado_direito, barco_lado_esquerdo):
    if barco_lado_esquerdo:
        print(f"""
                                                                                           
{lado_esquerdo} \==|==/~~~~~~~~~~~~~~~~~~~~ {lado_direito}""")
    else:
        print(f"""
                                                                                            
{lado_esquerdo} ~~~~~~~~~~~~~~~~~~~~\==|==/ {lado_direito} """)


