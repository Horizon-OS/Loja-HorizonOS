# Loja Horizon OS
<p align="center">
<img src="https://raw.githubusercontent.com/Horizon-OS/Loja-Horizon-OS/master/Logo/loja-horizon.png" alt="Logo" width="100" >
</p>
Esta loja é uma das aplicações desenvolvidas para a distribuição Horizon OS com o objetivo de simplificar a instalação de aplicações/programas Linux, e tornando o uso do 'Terminal' um pouco menos, embora seja muito útil.







# Atenção
Este repositório será atualizado semanalmente e comentado com todas as mudanças que ocorreram.
Para usar através deste repositório você deve ter os seguintes pacotes instalados em sua maquina Linux e também para funcionar deve instalar na pasta raiz do sistema da seguinte maneira /Programas/Loja-HorizonOS/

```bash
         gir1.2-webkit2-4.0
         python3-polib
         zenity
         python3-aptdaemon.gtk3widgets
         python3-aptdaemon
         python3-apt
         python3
         software-properties-gtk
         update-manager
```

Para sua segurança, não use o código-fonte da loja para uso final ainda, pois pode haver muitos bugs não reconhecidos para a sua distribuição que podem resultar na quebra dos pacotes de instalação do seu sistema!

# Instalação
Para instalar a versão estável da loja, você pode usar os seguintes comandos abaixo em seu terminal de comando:

Ubuntu e distribuições derivadas apenas
```bash
sudo add-apt-repository ppa:horizon-os/loja
sudo apt-get update
sudo apt-get install loja-horizon-os
```

## Licença
[GPLv3+](https://www.gnu.org/licenses/gpl-3.0.pt-br.html)

