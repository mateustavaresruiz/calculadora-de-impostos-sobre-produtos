def calcular_impostos():
    """
    Exemplo simples de cálculo de IPI, ICMS (por dentro), PIS e COFINS,
    editando diretamente no código.
    """
    
    # 1. Definição das variáveis básicas
    # ---------------------------------
    # Valor do produto (custo ou preço sem imposto)
    
    valor_produto = float(input("Digite o valor do Produto: "))
    
    # Alíquotas (em percentual). Exemplo: 5 significa 5%.
    aliquota_ipi = 5.00
    aliquota_icms = 18.00
    aliquota_pis = 1.65
    aliquota_cofins = 7.60
    
    # 2. Converter as alíquotas de % para decimal
    # -------------------------------------------
    aliq_ipi_dec = aliquota_ipi / 100  # ex.: 5% -> 0.05
    aliq_icms_dec = aliquota_icms / 100
    aliq_pis_dec = aliquota_pis / 100
    aliq_cofins_dec = aliquota_cofins / 100
    
    # 3. Cálculo do IPI (por fora)
    # -------------------------------------------
    # Valor do IPI = valor do produto * alíquota em decimal
    valor_ipi = valor_produto * aliq_ipi_dec
    
    # 4. Cálculo do ICMS (por dentro)
    # -------------------------------------------
    # Base ICMS = (valor_produto + valor_ipi) / (1 - aliq_icms_dec)
    base_icms = (valor_produto + valor_ipi) / (1 - aliq_icms_dec)
    
    # Valor do ICMS = base_icms * aliq_icms_dec
    valor_icms = base_icms * aliq_icms_dec
    
    # 5. Cálculo do PIS e COFINS (exemplo simplificado)
    # -------------------------------------------
    # PIS e COFINS (por fora, base = valor_produto, mas pode variar conforme regime).
    valor_pis = valor_produto * aliq_pis_dec
    valor_cofins = valor_produto * aliq_cofins_dec
    
    # 6. Calcular o total de impostos e o preço final
    # -------------------------------------------
    total_impostos = valor_ipi + valor_icms + valor_pis + valor_cofins
    preco_final = valor_produto + total_impostos
    
    # 7. Exibir resultados
    # -------------------------------------------
    print("===== CÁLCULO DE IMPOSTOS (EXEMPLO) =====")
    print(f"Valor do Produto:    R$ {valor_produto:,.2f}")
    print(f"Alíq IPI:            {aliquota_ipi:.2f}% | Valor IPI:    R$ {valor_ipi:,.2f}")
    print(f"Alíq ICMS:           {aliquota_icms:.2f}% | Base ICMS:    R$ {base_icms:,.2f} | Valor ICMS:  R$ {valor_icms:,.2f}")
    print(f"Alíq PIS:            {aliquota_pis:.2f}% | Valor PIS:    R$ {valor_pis:,.2f}")
    print(f"Alíq COFINS:         {aliquota_cofins:.2f}% | Valor COFINS: R$ {valor_cofins:,.2f}")
    print("-----------------------------------------")
    print(f"Total de Impostos:   R$ {total_impostos:,.2f}")
    print(f"Preço Final (aproximadamente): R$ {preco_final:,.2f}")

# Se quiser executar direto, chame a função:
if __name__ == "__main__":
    calcular_impostos()
