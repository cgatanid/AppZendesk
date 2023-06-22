import json

agentes = [
    {
        'Id': 373364218712,
        'Nombre': 'CARLA TOSSI',
        'Email': 'ctossi@anid.cl',
        'ListId': 1
    },
    {
        'Id': 373594117912,
        'Nombre': 'KARINA SILVA',
        'Email': 'ksilvab@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 373594188832,
        'Nombre': 'AYUDA BECAS',
        'Email': 'ayudabecas@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 373594197712,
        'Nombre': 'AYUDA FONDAP',
        'Email': 'ayudafondap@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 373594239132,
        'Nombre': 'AYUDA REC 2',
        'Email': 'ayudaredes2@anid.cl',
        'ListId': 1
    },
    {
        'Id': 373594246572,
        'Nombre': 'AYUDA FONDEQUIP',
        'Email': 'ayudafondequipq@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 373626516251,
        'Nombre': 'MARÍA ANTONIETA TAPIA',
        'Email': 'atapia@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 373626558431,
        'Nombre': 'AYUDA FONDECYT',
        'Email': 'ayudafondecyt@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 373626567551,
        'Nombre': 'AYUDA SIA',
        'Email': 'ayudasia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 373626572371,
        'Nombre': 'AYUDA PIA',
        'Email': 'ayudapia@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 373626583011,
        'Nombre': 'AYUDA INFORMACIÓN CIENTÍFICA',
        'Email': 'ayudaic@anid.cl',
        'ListId': 1
    },
    {
        'Id': 375343924492,
        'Nombre': 'AYUDA REC 1',
        'Email': 'ayudaredes1@anid.cl',
        'ListId': 1
    },
    {
        'Id': 376324678272,
        'Nombre': 'ANTONELLA CARVAJAL',
        'Email': 'carlatossi@gmail.com',
        'ListId': 1
    },
    {
        'Id': 378628465112,
        'Nombre': 'TAMARA SAZO',
        'Email': 'tsazo@anid.cl',
        'ListId': 1
    },
    {
        'Id': 378929628412,
        'Nombre': 'AYUDA DIPRES',
        'Email': 'ayudadipres@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 380810555471,
        'Nombre': 'BIANCA LEIVA',
        'Email': 'bleiva@anid.cl',
        'ListId': 1
    },
    {
        'Id': 385398220371,
        'Nombre': 'LEONARDO DEMANET M.',
        'Email': 'ldemanet@anid.cl',
        'ListId': 1
    },
    {
        'Id': 393470606632,
        'Nombre': 'FRANCESCA JAZMIN GOLDSCHMIDT O',
        'Email': 'fgoldschmidt@anid.cl',
        'ListId': 1
    },
    {
        'Id': 395002239712,
        'Nombre': 'AYUDA MILENIO',
        'Email': 'ayudamilenio@anid.cl',
        'ListId': 1
    },
    {
        'Id': 398670697392,
        'Nombre': 'EVELYN FIGUEROA',
        'Email': 'efigueroaa@anid.cl',
        'ListId': 1
    },
    {
        'Id': 400939641112,
        'Nombre': 'NATALIA VILCHES',
        'Email': 'nvilches@anid.cl',
        'ListId': 1
    },
    {
        'Id': 401183215412,
        'Nombre': 'CAROLINA ANDREA FREIRE TAPIA',
        'Email': 'cfreire@anid.cl',
        'ListId': 1
    },
    {
        'Id': 406239484192,
        'Nombre': 'VIVIANA ANDREA CÁCERES ALVEAL',
        'Email': 'vcaceres@anid.cl',
        'ListId': 1
    },
    {
        'Id': 406926284431,
        'Nombre': 'SANDRA ARMANDO',
        'Email': 'sarmando@anid.cl',
        'ListId': 1
    },
    {
        'Id': 407265479011,
        'Nombre': 'NANCY RUBIO',
        'Email': 'nrubio@anid.cl',
        'ListId': 1
    },
    {
        'Id': 409023729671,
        'Nombre': 'JOSE CIFUENTES',
        'Email': 'jcifuentes@anid.cl',
        'ListId': 1
    },
    {
        'Id': 410919410672,
        'Nombre': 'EDUARDO CONTRERAS GAILLARD',
        'Email': 'econtreras@anid.cl',
        'ListId': 1
    },
    {
        'Id': 412306327652,
        'Nombre': 'STAFF FISCALIA',
        'Email': 'staff_fiscalia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 413385679931,
        'Nombre': 'BERTA RIOS',
        'Email': 'brios@anid.cl',
        'ListId': 1
    },
    {
        'Id': 421004842672,
        'Nombre': 'MARITZA DONOSO',
        'Email': 'mfdonoso@anid.cl',
        'ListId': 1
    },
    {
        'Id': 421597189012,
        'Nombre': 'ANALISTAS UCR SPI 2',
        'Email': 'analistas2_ucr@anid.cl',
        'ListId': 1
    },
    {
        'Id': 421616667332,
        'Nombre': 'AYLEEN GARCÍA',
        'Email': 'agarcia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422185917972,
        'Nombre': 'EJECUTIVOS(AS) SIA',
        'Email': 'ejecutivos_tecnicos_sia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422321248512,
        'Nombre': 'FABIAN CIFUENTES',
        'Email': 'fcifuentes@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422322585172,
        'Nombre': 'JOHANA SANCHEZ',
        'Email': 'jsanchez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422324021292,
        'Nombre': 'MARIA REYES CASTRO',
        'Email': 'jreyes@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422324084972,
        'Nombre': 'ANALISTAS UCR',
        'Email': 'revisores_daf@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422365433651,
        'Nombre': 'ENCARGADO(A) TYE SIA',
        'Email': 'encargado_tye_sia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422365495971,
        'Nombre': 'ANALISTAS SIA',
        'Email': 'analistas_financieros_sia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422387814172,
        'Nombre': 'VICTOR ROCA',
        'Email': 'vroca@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422387862712,
        'Nombre': 'NORELIS REQUENA',
        'Email': 'nrequena@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422387902012,
        'Nombre': 'PATRICIA HERNANDEZ',
        'Email': 'phernandez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422445083672,
        'Nombre': 'CRISTIAN CAVIERES',
        'Email': 'ccavieres@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422445256272,
        'Nombre': 'EQUIPO TESORERÍA',
        'Email': 'tesoreria_staff@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422445287332,
        'Nombre': 'MARICEL MANCILLA',
        'Email': 'mmancilla@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422445421552,
        'Nombre': 'XIMENA ARCE',
        'Email': 'xarce@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422501645611,
        'Nombre': 'ANDREA ORTEGA',
        'Email': 'aortega@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422501668091,
        'Nombre': 'DENISSE ESTAY ECHEVERRIA',
        'Email': 'destay@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422504528991,
        'Nombre': 'ROBERTO ELIAS MARQUEZ JIMENEZ',
        'Email': 'rmarquez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422575080631,
        'Nombre': 'ALFREDO FERNANDEZ',
        'Email': 'afernandez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422575088591,
        'Nombre': 'CLAUDIA BERGER MORALES',
        'Email': 'cberger@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422575092931,
        'Nombre': 'MARÍA INÉS MENA QUIAN',
        'Email': 'mmena@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422575123791,
        'Nombre': 'MILEIDY GARCÍA BLANCO',
        'Email': 'mgarciab@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422575166911,
        'Nombre': 'OSCAR PACHECO',
        'Email': 'opacheco@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422575172611,
        'Nombre': 'SIMON PERNIA',
        'Email': 'spernia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422630051611,
        'Nombre': 'COORDINADOR CONTABILIDAD',
        'Email': 'contab_admin@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422882449192,
        'Nombre': 'ANDREA HERNANDEZ',
        'Email': 'ahernandezh@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422882530332,
        'Nombre': 'PATRICIA CONCHA',
        'Email': 'pconcha@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422882598272,
        'Nombre': 'ANGELINA PIZARRO',
        'Email': 'angelinap@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422882631092,
        'Nombre': 'GONZALO CUBILLOS',
        'Email': 'gcubillos@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422882787792,
        'Nombre': 'FRANCISCO CARREÑO',
        'Email': 'fcarreno@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422882803552,
        'Nombre': 'MARIBEL HERRERA',
        'Email': 'mherrera@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422882823112,
        'Nombre': 'LUCAS OSORIO',
        'Email': 'losorio@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422883484012,
        'Nombre': 'GENOVEVA RAMIREZ',
        'Email': 'gramirez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422883953412,
        'Nombre': 'JANIS ACEVEDO',
        'Email': 'jacevedo@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422884242152,
        'Nombre': 'EVELYN TORREALBA',
        'Email': 'etorrealba@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422885395632,
        'Nombre': 'APOYO ADMINISTRATIVO',
        'Email': 'apoyoadministrativo_sch@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422933271472,
        'Nombre': 'ASTRID FARIÑA',
        'Email': 'afarinav@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422933329892,
        'Nombre': 'JEANNETTE RUSSELL',
        'Email': 'jrussell@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422933524752,
        'Nombre': 'IVAN MUÑOZ',
        'Email': 'imunoz@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422933556712,
        'Nombre': 'LORETO VILLEGAS',
        'Email': 'mvillegas@anid.cl',
        'ListId': 1
    },
    {
        'Id': 422933563412,
        'Nombre': 'MACARENA FARIAS',
        'Email': 'mfarias@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423085925611,
        'Nombre': 'MARIO MAYORGA',
        'Email': 'mmayorga@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423085963691,
        'Nombre': 'NOELIA PEREZ',
        'Email': 'nperez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423086225851,
        'Nombre': 'VERONICA AGUIRRE',
        'Email': 'vaguirre@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423086942531,
        'Nombre': 'HEIDI GUZMAN',
        'Email': 'hguzman@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423087106871,
        'Nombre': 'RODRIGO MORA',
        'Email': 'rmora@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423087172111,
        'Nombre': 'PAUL NUÑEZ',
        'Email': 'pnunez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423087193291,
        'Nombre': 'DANIELLA PASTOR',
        'Email': 'dpastor@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139559511,
        'Nombre': 'PABLO BELLEI',
        'Email': 'pbellei@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139575931,
        'Nombre': 'OLAYA BASTIAS',
        'Email': 'obastias@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139625071,
        'Nombre': 'FELIX DIAZ',
        'Email': 'fdiaz@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139687731,
        'Nombre': 'VICTORINA NUÑEZ',
        'Email': 'vnunez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139711531,
        'Nombre': 'ALEJANDRA GAJARDO',
        'Email': 'agajardo@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139747471,
        'Nombre': 'PATRICIA ANDRADE',
        'Email': 'pandrade@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139766771,
        'Nombre': 'ALEJANDRA ECHEVERRIA',
        'Email': 'aecheverria@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139805871,
        'Nombre': 'ORLANDO DUVAL',
        'Email': 'oduval@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139867891,
        'Nombre': 'FELIPE VASQUEZ',
        'Email': 'fvasquez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423139977351,
        'Nombre': 'VALESKA TOBAR',
        'Email': 'vtobar@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423607040111,
        'Nombre': 'EQUIPO DOC UCR',
        'Email': 'ucr_docs@anid.cl',
        'ListId': 1
    },
    {
        'Id': 423978039672,
        'Nombre': 'ROCIO YANEZ RODRIGUEZ',
        'Email': 'ryanez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1903792339847,
        'Nombre': 'ENCARGADO(A) PROYECTOS SIA',
        'Email': 'encargada_proy_sia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1903792511647,
        'Nombre': 'EJECUTIVOS(AS) TYE SIA',
        'Email': 'ejecutivos_tye_sia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1903934877347,
        'Nombre': 'ELIZABETH VALENZUELA LEON',
        'Email': 'evalenzuela@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1903937732967,
        'Nombre': 'VERONICA CACERES',
        'Email': 'vcaceresm@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904055824487,
        'Nombre': 'SUSANA CASTRO',
        'Email': 'scastro@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904073928807,
        'Nombre': 'STAFF PREMIOS',
        'Email': 'premios_anid@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904182405631,
        'Nombre': 'EQUIPO COMERCIALIZACION',
        'Email': 'comercializacion@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904221818967,
        'Nombre': 'EQUIPO DPC',
        'Email': 'equipodpc@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904469474191,
        'Nombre': 'EQUIPO IMAGEN',
        'Email': 'equipo_imagen@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904501067551,
        'Nombre': 'AUXILIAR DEPARTAMENTO FINANCIERO',
        'Email': 'auxiliar_financiero@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904631317631,
        'Nombre': 'ALICIA BRAVO',
        'Email': 'abravo@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904715127551,
        'Nombre': 'MARIA LORETO RAMIREZ',
        'Email': 'mramirez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904720211407,
        'Nombre': 'AYUDA PROYECTOS INSTITUCIONALES',
        'Email': 'ayudapi@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904781266971,
        'Nombre': 'CARLOS ORTIZ',
        'Email': 'cortiz@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904886028007,
        'Nombre': 'EQUIPO OREALC',
        'Email': 'orealcsud@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1904892790331,
        'Nombre': 'CATALINA ROMERO',
        'Email': 'cromero@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905013553051,
        'Nombre': 'ALEJANDRA ACUÑA',
        'Email': 'aacuna@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905084984911,
        'Nombre': 'JORGE BARROS',
        'Email': 'jbarros@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905160647711,
        'Nombre': 'CONSEJEROS FONDECYT',
        'Email': 'consejeros_fondecyt@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905199481911,
        'Nombre': 'CLAUDIO CONTRERAS',
        'Email': 'ccontreras@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905202449071,
        'Nombre': 'STAFF COOPERACION INTERNACIONAL',
        'Email': 'cooperacion_internacional@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905205535807,
        'Nombre': 'ANALISTAS GPE',
        'Email': 'analistas_gpe@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905209301767,
        'Nombre': 'ANGELINA GUTIERREZ',
        'Email': 'agutierrez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905256047127,
        'Nombre': 'ALEXIS HERNANDEZ',
        'Email': 'ahernandezp@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905260515527,
        'Nombre': 'ESTEBAN GONZALEZ',
        'Email': 'egonzalez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905266526727,
        'Nombre': 'EQUIPO CONICYT REGIONES',
        'Email': 'conicytregiones@conicyt.cl',
        'ListId': 1
    },
    {
        'Id': 1905268112627,
        'Nombre': 'STAFF ANID',
        'Email': 'staff_anid@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905304712411,
        'Nombre': 'JAVIER MALDONADO',
        'Email': 'jmaldonado@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905305181311,
        'Nombre': 'EQUIPO REDES',
        'Email': 'redes@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905306782287,
        'Nombre': 'PAULA LUCENA',
        'Email': 'plucena@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905326254367,
        'Nombre': 'CARMEN ALEGRIA',
        'Email': 'calegria@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905385986791,
        'Nombre': 'EMILIO CERDA',
        'Email': 'ecerda@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905481610151,
        'Nombre': 'STAFF GEP',
        'Email': 'staff_gep@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905542331767,
        'Nombre': 'CARMEN GLORIA MARTINEZ',
        'Email': 'cmartinez@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905550658407,
        'Nombre': 'MIGUEL MEZA',
        'Email': 'mmeza@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905586107551,
        'Nombre': 'EQUIPO REDIAM',
        'Email': 'rediam@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905670457951,
        'Nombre': 'CAROLINA NEIRA',
        'Email': 'cneira@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905672357007,
        'Nombre': 'ELIANA NEME',
        'Email': 'eneme@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905697697511,
        'Nombre': 'ERNESTO NOVOA',
        'Email': 'enovoa@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905732307851,
        'Nombre': 'CAMILA OYARZUN',
        'Email': 'coyarzun@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905736372927,
        'Nombre': 'CONSTANZA PARDO',
        'Email': 'cpardo@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905766981807,
        'Nombre': 'STAFF PROGRAMA BECAS FUNDACIÓN CARLOS S',
        'Email': 'becas_fcs@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905767862411,
        'Nombre': 'CONSTANZA PEIRANO',
        'Email': 'cpeirano@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905794005631,
        'Nombre': 'CONSULTORÍA',
        'Email': 'consultoria@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905800412111,
        'Nombre': 'PAULINA QUEZADA',
        'Email': 'pquezada@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905805314511,
        'Nombre': 'JUAN ROMAN',
        'Email': 'jroman@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905831824271,
        'Nombre': 'STAFF SOCIEDAD',
        'Email': 'sociedad@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905847729271,
        'Nombre': 'GERARDO SOTO',
        'Email': 'gsoto@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905851595071,
        'Nombre': 'ISABEL STERN',
        'Email': 'istern@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905861106751,
        'Nombre': 'ALEJANDRA SUAZO',
        'Email': 'asuazo@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905862749991,
        'Nombre': 'ENZO TAPIA',
        'Email': 'etapia@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905873702687,
        'Nombre': 'VANESSA TORRES',
        'Email': 'vatorres@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905897697231,
        'Nombre': 'CLAUDIA TRIGO',
        'Email': 'ctrigo@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905913258431,
        'Nombre': 'SUSANA URIBE',
        'Email': 'suribe@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905953361327,
        'Nombre': 'KATHERINE VEGA',
        'Email': 'kvega@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905992445007,
        'Nombre': 'EQUIPO VENTANILLA',
        'Email': 'ventanilla@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1905998568007,
        'Nombre': 'VICTOR VIVANCO',
        'Email': 'vvivanco@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1906004699007,
        'Nombre': 'YULIANA ZAMORA',
        'Email': 'yzamora@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1906014079271,
        'Nombre': 'RAFAEL ZAPATA',
        'Email': 'rzapata@anid.cl',
        'ListId': 1
    },
    {
        'Id': 1906014477551,
        'Nombre': 'YALYNA ZEPEDA',
        'Email': 'yzepeda@anid.cl',
        'ListId': 1
    }
]


# Guardar como archivo JSON
with open('agentes.json', 'w') as json_file:
    json.dump(agentes, json_file)