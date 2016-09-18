#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)

def drop_db():
    if 'om' in connection.database_names():
        db = connection.drop_database('om')
        print('[+] om database removed.')

def insert_users():
    db = connection.om
    users = db.users
    newlog = {  "username": "newlog",
                "description": "",
                "social_networks": {"twitter": "@newlog_", "github": "newlog"},
                "mail": "newlog@overflowedminds.net",
                "img":"me.png",
                "pk":
                """
                -----BEGIN PGP PUBLIC KEY BLOCK-----<br>
                Version: SKS 1.1.4<br>
                Comment: Hostname: pgp.mit.edu<br>
                <br>
                mQGiBE/ctckRBACY1zCOmK1oCufr1FBnwT63hROslcKYqD/hbHfPuZEBmJ/kQFm4q+xI23P5<br>
                4dmiqfLanq03nfpkRkkAWQ8UNBXA/d7RbaCoQtZJ8PKOrd1r0vc7sWPi7rkdyRIAaX4EYlQh<br>
                czzvknhHH9kfITsOy32e4/9gPUrJeCjE0D9YJmRI7wCg5X9r0+gs9vGbBo0jZ5SfTNw81FED<br>
                /j40+aYtLrAivrluYTDYxtGgmSsQ5EH9a5rQrjP6HNhGa02ky5gWN/9ulCVWnQCEk/rMWx/t<br>
                QYm2R9KgL837AZ5ejAPW9A4RxOCjdcgkPd1fECSj6VuLVqQ1eJvu7WprbFKSrsHzdU9DmvDH<br>
                OOEFGElgXEZG19yfQcB/1jIkZT32A/0VpkBZDon+jcLMk7enNFRZBnoibssOnvihSqtT2vqX<br>
                DJOu7vPLwZPIUSjJqNZmn7mxzcGMZ29PTnfl/txis/YUbw6UvZgzumTjE0pIhsYeGO27Lbxc<br>
                LoS9jJuhbqpUFJPo6FjNyIzymFI9/OH5Sz5yIa9U315pvITXwzzLC0CJRLQ2TmV3bG9nIChP<br>
                dmVyZmxvd2VkIE1pbmRzKSA8bmV3bG9nQG92ZXJmbG93ZWRtaW5kcy5uZXQ+iGAEExECACAF<br>
                Ak/ctckCGwMGCwkIBwMCBBUCCAMEFgIDAQIeAQIXgAAKCRB8oi5A7uWkRy6cAJ9IHtktUnpz<br>
                GIh8RPgqSzSfhBpz+ACgkTwtKy0qCl8MebQE+eZRuACHF1q5Ag0ET9y1yRAIALUTzwHDgyXs<br>
                HkFXYNo7h9abNzUjjAnVuijcWHqcS180UDLCpCKR0WMR9DbY7tNA7zY+WNVPtWdFYCY6XsTE<br>
                0D7D6NBHO3b3Ln7VL9fQBvgsgtGl4h/azMDpwOuu03cPmA2Ve+CVH1/ckxGyjc9Ikcv/Q+NQ<br>
                P4kQkhWo5dhzdhYSuv3HaNCqNLn+y6QHv3hLyFdIzj2LX7GKwIfQTZdkreyxaFiXZSsfNQuV<br>
                cfaxTaMK7CaEZFgIoT2ZcJGRBRZnvH4G6cqblpCPf3KlXlg42q2dLxt5xAmW8ucCtA97gv1I<br>
                GxAq3VLh37ysF2c7n1RK2tTpdxBG0L4dYi+IPO/I/rsAAwUIAIuwhy3sI0iAO74YxrRUmPr0<br>
                6bKpN460/Sxk3JjNdLXUXDItudz2hP0szcu/CUKsGlfZyldRZmmCIV3axYCietAWBXvIvoN/<br>
                ujGb3WFuyb+rS85itj5osysjQomj2yO9KcX6HlFZQBvu8EUnhdVUG4zLkJOJdPEQOgZMA4fN<br>
                IiVDmChXmgsMVUPLeuV9/2LlQzkIzH4zhX2vg8on/JGXY1XQLJu2ToWTp2pgNT2mmvD8B3C8<br>
                HwmfCUcTrQB6YzNNKxH8RBgvq6JnRDJGRJo4at7DV1B68dnkcXBqdrefXdShyOAMyjiqZxcA<br>
                MeuszPI+fBK++LiAP3hq26fmEALgeoWISQQYEQIACQUCT9y1yQIbDAAKCRB8oi5A7uWkR9do<br>
                AKCrCCs7F8nUSP6Mk4Jzh39ih/iRBwCdFcnurZkyhvur5QYSZKglhZlcKTk=<br>
                =o/xe<br>
                -----END PGP PUBLIC KEY BLOCK-----<br>
                """
             }
    vlan7 = {   "username": "vlan7",
                "description": "",
                "social_networks": {},
                "mail": "vlan7@overflowedminds.net",
                "img": "",
                "pk":""
             }
    try:
        users.insert(newlog)
        users.insert(vlan7)
        print('[+] Users inserted to database om in users collection')
    except Exception as e:
        print("Unexpected error: {0}".format(e))

def insert_papers():
    db = connection.om
    papers = db.papers
    paper1 = { "username": "newlog",
            "title": "Introducción a la Explotación de Software en sistemas Linux",
            "path": "static/files/newlog/papers/introduccion_explotacion_software_linux.pdf",
            "description": "Este documento es una extensa introducción al mundo del shellcoding y exploiting en Linux.",
            "date": "12/10/2009"
          }
    paper2 = { "username": "newlog",
            "title": "Estudio y explotación del sistema de gestión de memoria dinámica en sistemas GNU/Linux",
            "path": "static/files/newlog/papers/linux_heap_exploiting_revisited.pdf",
            "description": "Este documento detalla el funcionamiento del sistema de gestión de memoria dinámica de Linux y diferentes técnicas para atacar dichos algoritmos. Aquí se puede encontrar un <a href='http://vimeo.com/70799803'>vídeo</a> de la presentando el trabajo en la rootedcon 2013.",
            "date": "27/11/2012"
          }
    paper3 = { "username": "vlan7",
            "title": "0x01 Local Linux x86 Shellcoding Without Any High Level Language",
            "path": "static/files/vlan7/papers/0x01_local_linux_x86_shellcoding_without_any_high_level_language.pdf",
            "description": "Este documento introduce conceptos básicos sobre shellcoding en Linux. También tienes una demostración en <a href='static/files/vlan7/papers/0x01_shellcoding.mp4'>vídeo</a>.",
            "date": "07/11/2010"
          }
    paper4 = { "username": "vlan7",
            "title": "0x02 Bypassing Local Linux x86 ASLR Protection",
            "path": "static/files/vlan7/papers/0x02_bypassing_local_Linux_x86_ASLR_protection.pdf",
            "description": "Este documento explica una técnica para evadir ASLR en Linux a través de saltar a la sección de código del binario. También tienes una demostración en <a href='static/files/vlan7/papers/Shellcoding_y_Urban_Dogs.mp4'>vídeo</a>.",
            "date": "27/02/2011"
          }
    paper5 = { "username": "vlan7",
            "title": "0x03 Bypassing Remote Linux x86 ASLR Protection",
            "path": "static/files/vlan7/papers/0x03_bypassing_Remote_Linux_x86_ASLR_protection.pdf",
            "description": "Este documento explica una técnica para evadir ASLR en Linux de manera remota a través de saltar a la sección de código del binario.",
            "date": "22/04/2012"
          }
    paper6 = { "username": "vlan7",
            "title": "0x4 Bypassing Local Linux x86 ASLR Protection Revisited",
            "path": "static/files/vlan7/papers/0x04_bypassing_local_Linux_x86_ASLR_protection_revisited.pdf",
            "description": "Este documento explica una técnica para evadir ASLR en Linux a través de saltar a la sección de código del binario y realizar una ataque de fuerza bruta.",
            "date": "21/04/2012"
          }
    try:
        papers.insert(paper6)
        papers.insert(paper5)
        papers.insert(paper4)
        papers.insert(paper3)
        papers.insert(paper2)
        papers.insert(paper1)
        print('[+] Papers inserted to database om in papers collection')
    except Exception as e:
        print("Unexpected error: {0}".format(e))

def insert_exploits():
    db = connection.om
    exploits = db.exploits
    xpl1 = { "username": "newlog",
            "title": "cve-2008-5405",
            "path": "https://github.com/newlog/exploiting/tree/master/training/windows/exploits/cve-2008-5405_cain",
            "description": "Stack-based buffer overflow in the RDP protocol password decoder in Cain & Abel 4.9.23 and 4.9.24, and possibly earlier, allows remote attackers to execute arbitrary code via an RDP file containing a long string.",
            "date": "01/10/2014"
          }
    xpl2 = { "username": "newlog",
            "title": "cve-2009-1831",
            "path": "https://github.com/newlog/exploiting/tree/master/training/windows/exploits/cve-2009-1831_winamp",
            "description": "The Nullsoft Modern Skins Support module (gen_ff.dll) in Nullsoft Winamp before 5.552 allows remote attackers to execute arbitrary code via a crafted MAKI file, which triggers an incorrect sign extension, an integer overflow, and a stack-based buffer overflow.",
            "date": "01/10/2014"
          }
    xpl3 = { "username": "newlog",
            "title": "cve-2011-0257",
            "path": "https://github.com/newlog/exploiting/tree/master/training/windows/exploits/cve-2011-0257_quicktime",
            "description": "Integer signedness error in Apple QuickTime before 7.7 allows remote attackers to execute arbitrary code or cause a denial of service (application crash) via a crafted PnSize opcode in a PICT file that triggers a stack-based buffer overflow.",
            "date": "01/10/2014"
          }
    xpl4 = { "username": "newlog",
            "title": "cve-2012-5691",
            "path": "https://github.com/newlog/exploiting/tree/master/training/windows/exploits/cve-2012-5691_realplayer",
            "description": "Buffer overflow in RealNetworks RealPlayer before 16.0.0.282 and RealPlayer SP 1.0 through 1.1.5 allows remote attackers to execute arbitrary code via a crafted RealMedia file.",
            "date": "01/10/2014"
          }
    xpl5 = { "username": "newlog",
            "title": "cve-2012-4792",
            "path": "https://github.com/newlog/exploiting/tree/master/training/windows/exploits/cve-2012-4792_ie8",
            "description": "Use-after-free vulnerability in Microsoft Internet Explorer 6 through 8 allows remote attackers to execute arbitrary code via a crafted web site that triggers access to an object that (1) was not properly allocated or (2) is deleted, as demonstrated by a CDwnBindInfo object, and exploited in the wild in December 2012.",
            "date": "01/10/2014"
          }
    try:
        exploits.insert(xpl5)
        exploits.insert(xpl4)
        exploits.insert(xpl3)
        exploits.insert(xpl2)
        exploits.insert(xpl1)
        print('[+] Exploits inserted to database om in exploits collection')
    except Exception as e:
        print("Unexpected error: {0}".format(e))

def insert_tools():
    db = connection.om
    tools = db.tools
    tool1 = { "username": "newlog",
            "title": "Find Trampoline",
            "path": "https://github.com/newlog/exploiting/tree/master/scripts/immunity/findtrampoline",
            "description": "This tool is used as an Immunity Debugger plugin to find jmp <reg> like instructions from a crash point. You can find an extended description following the link.",
            "date": "01/08/2014"
          }
    tool2 = { "username": "newlog",
            "title": "Break On DLL Load",
            "path": "https://github.com/newlog/exploiting/tree/master/scripts/immunity/break_dll_load",
            "description": "This tool is used as an Immunity Debugger plugin that lets you break on a delayed DLL load and break on an specific address of this DLL.",
            "date": "02/08/2014"
          }
    try:
        tools.insert(tool2)
        tools.insert(tool1)
        print('[+] Tools inserted to database om in tools collection')
    except Exception as e:
        print("Unexpected error: {0}".format(e))

def insert_quotes():
    db = connection.om
    quotes = db.quotes
    with open('quotes.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.find(':::') != -1:
                d = line.split(':::')
                quote = {'quote': d[0].strip(), 'author': d[1].strip()}
                try:
                    quotes.insert(quote)
                except Exception as e:
                    print("Unexpected error inserting {0}: {1}".format(quote, e))
    print('[+] Quotes inserted to database om in quotes collection')

def create_db():
    drop_db()
    insert_users()
    insert_papers()
    insert_exploits()
    insert_tools()
    insert_quotes()

create_db()
