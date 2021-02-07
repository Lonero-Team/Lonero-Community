Main Installation Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   Sketch Plugin: wget https://git.io/Jv2pk
   Use Julia: Pkg.add("DecentralizedInternet")
   Install via NPM: npm i decentralized-internet
   Install via DUB: dub add decentralized-internet
   Install via YARN: yarn add decentralized-internet
   Install via PIP: pip install decentralized-internet
   Install via APM: apm install decentralized-internet
   Install via GEM: gem install decentralized-internet
   Install via PNPM: pnpm install decentralized-internet
   Install via CNPM: cnpm install decentralized-internet
   Ember Installation: ember install decentralized-internet   
   Install via Spack: ./spack install decentralized-internet
   Raco Installation: raco pkg install decentralized-internet
   Install w/ Meteor: meteor add startup:decentralized-internet
   Install via VS Code: ext install Lonero.decentralized-internet
   Other Meteor Method: meteor npm install decentralized-internet   
   Install through Leiningen/Boot: [decentralized-internet "0.1.0"]
   Install via SNAP: sudo snap install decentralized-internet --edge
   Install via Bower: bower install Lonero-Team/Decentralized-Internet
   Docker Installation: docker pull gamer456148/decentralized-internet
   Use Clojure CLI/deps.edn: decentralized-internet {:mvn/version "0.1.0"}
   Use Gradle:Compile 'decentralized-internet:decentralized-internet:0.1.0'
   SourceForge: git clone git://git.code.sf.net/p/decentralized-internet/git
   Use wget: sudo wget -O decentralized-internet.tar.gz "https://git.io/JvR7b"

--------------

| **Sysget Users**
| ``sysget install decentralized-internet``
| *Pick either option: 4, 14, 15, 18 or 20*

--------------

| **Using Maven**

::

   <dependency>
     <groupId>decentralized-internet</groupId>
     <artifactId>decentralized-internet</artifactId>
     <version>0.1.0</version>
   </dependency>

--------------

| **Install via Dart**  
| Add to your pubspec.yaml file:
::

   dependencies:
     decentralized_internet: ^3.4.1
Run: ``pub get``

--------------

| **Install via Cordova**
::

   cordova plugin add https://github.com/Lonero-Team/Decentralized-Internet.git
   Or cordova plugin searchcordova-plugin-decentralized-internet
   Or cordova plugin add cordova-plugin-decentralized-internet

--------------

| **Export Components**
::

   bit export decentralized-internet.lonero_decentralized-internet

--------------

| **Use this Module via Puppet**
| Add this to your Puppetfile as a declaration:
| ``mod 'gamer456148-decentralized_internet', '5.2.1'``
| Next run the command:
| ``bolt puppetfile install``
| Instead of the above, you can also try adding:
| ``mod 'gamer456148-decentralized_internet', '5.2.1'``
| This mod line is for those who use r10k or Code Manager
| Learn more `here`_

--------------

| **Arch Linux Installation Method**  
::

   git clone https://aur.archlinux.org/snapd.git
   cd snapd
   makepkg -si
   sudo systemctl enable --now snapd.socket
   sudo ln -s /var/lib/snapd/snap /snap
   sudo snap install decentralized-internet --edge
   
--------------

**For Installing on** `DigitalOcean`_ 
---------------------------------------

*Please keep in mind as of the time of writing this, our SDK is not yet live on the DigialOcean Marketplace*

**First Step:** \
In order to install via one click app, *(When available)*,
click the "Create Droplet Button" via the `Marketplace`_ page.

**Second Step:** \
In regards to usage, I recommend reading our SDK's
generic usage guide `that is here`_. The same instructions apply to
droplets.

Please keep in mind you can skip the ```npm install```, as the node modules should already be pre-installed in the droplet but not the below configurations.

To access the program in root use ```cd node_modules/decentralized-internet```. The dev files should be in ```cd addon```. You can then install the below configurations in root, and proceed with the core component development.


**Configurations:** \
For ease of simplicity, I recommend installing the `Slap IDE`_ over VIM or GNU Nano. \
::

   curl -sL https://raw.githubusercontent.com/slap-editor/slap/master/install.sh | sh

Also keep in mind if you decide to use slap, it utilizes Node.js so make sure you have the latest version installed: 
::

   sudo npm install -g slap@latest
   
You can now run the Slap commands seen `at their repo`_, for editing code files. For HaXe, I recommend you do the default PPA Ubuntu Installation:

::

   sudo add-apt-repository ppa:haxe/releases -y
   sudo apt-get update
   sudo apt-get install haxe -y
   mkdir ~/haxelib && haxelib setup ~/haxelib

Or run the Debain installation:

::

   sudo apt-get install haxe -y
   mkdir ~/haxelib && haxelib setup ~/haxelib

The rest of the configuration instructions in regards to Debian, can be
seen `at the HaXe site`_.
 | After you install Slap and Haxe on the Droplet, I recommend you use Slap for editing needed code files, and the ``haxelib`` commands in the terminal in regards to HaXe code files.

--------------

This project was created in order to support a new internet. One that is
more open, free, and censorship-resistant in comparison to the old
internet. An internet that eventually wouldn’t need to rely on telecom
towers, an outdated grid, or all these other “old school” forms of tech.
We believe P2P compatibility is an important part of the future of the
net. Grid Computing also plays a role in having a better means of
transferring information in a speedy, more cost-efficient and reliable
manner.

|Mac| |N|ChromeStore| |N|UptoDownDroid| |N|OperaDownload| |GooglePlay|

`GetJar`_ `Soft32`_ `GitLab`_ `Aptoide`_ `Softpile`_ `TideLift`_ `AppAgg`_ `Apptoko`_ `GitHub App`_ `Stackshare`_ `AlternativeTo`_ `Software Informer`_

**For citing this software:**

Kamal, A. M. decentralized-internet. npm (2020). Available at: https://www.npmjs.com/package/decentralized-internet. (Accessed: 30th September 2020)

.. _chainboard--the-next-gen-wireless-dev-board:
.. _here: https://puppet.com/docs/pe/2019.2/managing_puppet_code.html   
.. _DigitalOcean: https://www.digitalocean.com/
.. _Marketplace: https://marketplace.digitalocean.com/
.. _that is here: https://lonero.readthedocs.io/en/latest/Decentralized%20Internet%20Docs/Critical%20Components.html
.. _Slap IDE: https://github.com/slap-editor/slap
.. _at their repo: https://github.com/slap-editor/slap#usage
.. _at the HaXe site: https://haxe.org/download/linux/   
.. |Mac| image:: https://jaywcjlove.github.io/sb/download/macos.svg
   :target: https://git.io/Jv2pv
.. |N|ChromeStore| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/chromewebstore_badgewborder_v2.png
   :target: https://chrome.google.com/webstore/detail/decentralized-internet-sd/gdomaijaeldibcpllgjfimjgdjngojig   
.. |N|UptoDownDroid| image:: https://stc.utdstc.com/img/download-uptodown8.png
   :target: https://decentralized-internet.en.uptodown.com/android   
.. |N|OperaDownload| image:: https://raw.githubusercontent.com/Mentors4EDU/Images/master/opera(1).png
   :target: http://android.oms.apps.bemobi.com/en_us/decentralized_internet.html
.. |GooglePlay| image:: https://jaywcjlove.github.io/sb/download/googleplay.svg
   :target: https://play.google.com/store/apps/details?id=com.asamkmm.SLTJ
.. _GetJar: https://www.getjar.com/categories/tool-apps/Decentralized-Internet-976910
.. _Soft32: https://decentralized-internet.soft32.com/
.. _GitLab: https://gitlab.com/decentralizedinternet/Decentralized-Internet
.. _Aptoide: https://decentralized-internet-sdk.en.aptoide.com/
.. _Softpile: https://www.softpile.com/decentralized-internet/
.. _TideLift: https://www.minds.com/newsfeed/1100003685079408640?referrer=LoneroLNR
.. _AppAgg: https://appagg.com/android/communication/decentralized-internet-sdk-34450780.html?hl=en
.. _Apptoko: https://apptoko.com/android/search?keyword=com.asamkmm.SLTJ
.. _GitHub App: https://github.com/apps/decentralized-internet
.. _Stackshare: https://stackshare.io/decentralized-internet
.. _AlternativeTo: https://alternativeto.net/software/decentralized-internet/
.. _Software Informer: https://decentralized-internet.software.informer.com/
