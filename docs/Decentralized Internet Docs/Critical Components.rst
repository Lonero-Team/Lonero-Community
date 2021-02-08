Documentation
==============
|npm| \| |Crates.io| \| |Discord|
\| |Gitter| \| |Read the Docs|

Critical Components
~~~~~~~~~~~~~~~~

-  Tools and Protocols
-  Distributed Computing
-  Decentralized Web Model

Basic Usage Introduction
~~~~~~~~~~~~~~~~~~~~~~~~

This is the same usage guide that is available in `LeanPub`_ and `other`_ places.

One way to get started is by installing the SDK. Let us start by
running:

::

   npm install decentralized-internet

Now let us:

::

   $ cd node_modules
   $ cd decentralized-internet
   $ ls

Now, multiple folders are setup for routing, but the easiest folder to
cd into for looking at the components is addon so:

::

   $ cd addon
   $ ls

Now you can see there are four main components to this project:

-  CluserPost
-  GridBee
-  LNRChain
-  Reinvent the Internet

Those are the core folder/component names of what we will be looking at.

**What is Clusterpost?**

`Clusterpost`_ is a grid computing tool that allows you to offload
processes to a CouchDB database. However, for this SDK the migration is
suggesting to use `BigChainDB`_ over CouchDB on the basis of
decentralization opportunities. Clusterpost is also utilized for
remotely scheduling and executing computational processes.

Here you can look at the code so:

::

   $ cd clusterpost
   $ sudo ./setUpDevelopment.sh
   $ sudo nano conf.production.json

Let us start with looking at the following configs in the
conf.production.json file

.. code:: JSON

   {
       "host": "localhost",
       "port": 8180,
       "plugins": {
           "vision": {},
           "inert": {},
           "lout": {},
           "h2o2": {},
           "hapi-auth-jwt": {},
           "clusterpost-auth": {
               "privateKey": "someRandomKey",
               "saltRounds": 10,
               "algorithm": {
                   "algorithm": "HS256"
               },
               "algorithms": {
                   "algorithms": [ "HS256" ]
               },

Here, you see the default port it should run on is 8180, you are welcome
to change that if needed or open the port. Also you see the plugins or
default NPM packages the production environment uses and the default
algorithm for clusterpost's authentication.

Next let us change the credentials as needed:

.. code:: JSON

   },
               "mailer": {
                   "nodemailer": "nodemailer-stub-transport",
                   "from": "clusterpost server <insertemail@here.com>",
                   "message": "Hello @USERNAME@,<br>Somebody asked me to send you a link to reset your password, hopefully it was you.<br>Follow this <a href='@SERVER@/public/#/login/reset?token=@TOKEN@'>link</a> to reset your password.<br>The link will expire in 30 minutes.<br>Bye."
               },
               "userdb" : {
                   "hostname": "http://localhost:5984",
                   "database": "clusterjobs"
               }
           },

You need to setup the login either through nodemailer or the database
program you are using and change the credentials so that clusterpost
will be able to authenticate into the database.

Next while running the database you could run some tests, so:

::

   $ cd test
   $ nautilus .

You are free to look into the configs and test code as needed, but you
can get started testing the default setup right away running:
``npm run`` or ``node filename.js``

A good example would be

::

   $ cd test
   $ node createNewJob.js
   
**The GridBee Framework**

Now, let us take a look at the GridBee Framework, which is an open
source library that allows web browsers to act as clients and
communicate with BOINC. It is coded in JavaScript and the HaXe
programming language.

Make sure to download `HaXe`_ and `FlashDevelop`_. FlashDevelop is an
IDE but is needed to compile the project file GridBee.hxproj.

If you are still in the clusterpost test folder then here is what to run
in the terminal:

::

   $ cd ../
   $ cd ../
   $ cd gridbee-framework-old
   $ cd GridBee
   $ nauilus .

Now you can see the project file GridBee.hxproj, right click it to open
w/ FlashDevelop and press F8 to build.

You can also merge local storage with the BigChainDB that clusterpost is
utilizing, and http requests to offload processes from your application
and start optimally building a pipeline, but this is beyond the scope of
this introduction.

**Let's Look at LNRChain**

The LNRChain folder includes tendermint, and the basic app.js demo file,
and is meant to be utilized for:

1) Part of a pipeline where you can connect Tendermint to BigChainDB
   *OR*
2) A `sidechain`_ for the SDK and `LNRBeta`_ and `Bitcoin`_.

To access LNRChain, if you are still in the GridBee folder:

::

   $ cd ../
   $ cd ../
   $ cd LNRChain
   $ sudo chmod 777 tendermint
   $ sudo nano app.js

Now you have just opened the app.js sample in the terminal, you should
see:

.. code:: Javascript

   // app.js
   let lotion = require('lotion')

   let app = lotion({
       initialState: {
           count: 0
       }
   })

   function transactionHandler(state, transaction) {
       if (state.count === transaction.nonce) {
           state.count++
       }
   }

   let connect = require('lotion-connect')
   app.use(transactionHandler)

   app.start().then(appInfo => console.log(appInfo.GCI))

This is Lotion's multi-state sample file which allows you to run
multiple states for the blockchain project you want to setup. Lotion is
the npm module powered by the Tendermint consensus for you to make your
own blockchain apps.

**Component #4: Reinvent the Net**

Now is time for the final core component of this SDK. Let us start by
accessing the source files:

::

   $ cd ../
   $ cd Reinvent-the-Internet
   $ unzip The APIs & Shell.zip
   $ nautilus .

Let us open the MSP430G2001.ccxml file with a text editor, i.e. "right
click":

.. code:: XML

   <?xml version="1.0" encoding="UTF-8" standalone="no"?>
   <configurations XML_version="1.2" id="configurations_0">
       <configuration XML_version="1.2" id="configuration_0">
           <instance XML_version="1.2" desc="TI MSP430 USB1" href="connections/TIMSP430-USB.xml" id="TI MSP430 USB1" xml="TIMSP430-USB.xml" xmlpath="connections"/>
           <connection XML_version="1.2" id="TI MSP430 USB1">
               <instance XML_version="1.2" href="drivers/msp430_emu.xml" id="drivers" xml="msp430_emu.xml" xmlpath="drivers"/>
               <platform XML_version="1.2" id="platform_0">
                   <instance XML_version="1.2" desc="MSP430G2001" href="devices/MSP430G2001.xml" id="MSP430G2001" xml="MSP430G2001.xml" xmlpath="devices"/>
               </platform>
           </connection>
       </configuration>
   </configurations>

The fourth module (as one can tell), is hardware-oriented. The XML
config shows that the driver is for a Texas Instruments dev board. This
also means that the IDE that the fourth component was developed on was
likely `CCS Cloud`_.

Now you may be confused at this point as to what was the point of this
module or what is it even for?

This part of the project was actually utilized for a hardware project in
which somebody garnished underwater wireless signals through sonar
conversion. However, similar use-cases can be done for anybody who wants
to have a software defined network. This is your chance to expand the
pipeline through low level hardware or code integrations and an optional
part of the SDK.

   To summarize we are:

1) Offloading data
2) Communicating Data
3) Building our Blockchain
4) Building our own SDN and wireless protocol

This is why things have been setup the way they are.   

.. |npm| image:: https://img.shields.io/npm/dt/decentralized-internet?label=NPM%20Downloads
.. |Crates.io| image:: https://img.shields.io/crates/d/decentralized-internet?label=crates.io%20Downloads
.. |Discord| image:: https://img.shields.io/discord/639489591664967700
   :target: https://discord.gg/buTafPc
.. |Gitter| image:: https://img.shields.io/gitter/room/Decentralized-Internet/community
   :target: https://gitter.im/Decentralized-Internet/community?source=orgpage
.. |Read the Docs| image:: https://img.shields.io/readthedocs/lonero
   :target: https://lonero.readthedocs.io/en/latest/
.. _LeanPub: https://leanpub.com/futurism   
.. _other: https://hackaday.io/project/171604-building-a-decentralized-internet   
.. _Clusterpost: https://github.com/juanprietob/clusterpost
.. _BigChainDB: https://github.com/bigchaindb/bigchaindb/tree/tendermint-backward-compat   
.. _HaXe: https://haxe.org/
.. _FlashDevelop: https://www.flashdevelop.org/
.. _sidechain: https://medium.com/@jaekwon/cosmos-creating-interoperable-blockchains-part-1-2929435ba1fa
.. _LNRBeta: https://github.com/Lonero-Team/Lonero-Beta
.. _Bitcoin: https://github.com/bitcoin/bitcoin
.. _CCS Cloud: https://dev.ti.com/
