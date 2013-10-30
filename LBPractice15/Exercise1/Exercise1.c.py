def main():
    snk = {}
    snk['Kalle'] = 15234
    snk['Jarmo'] = 777712
    if 'Jarmo' in snk:
        print(snk['Jarmo'])
    else:
        print("Jarmo was not found from the dictionary")
main()
