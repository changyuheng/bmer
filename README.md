bmer
----
a command line user ofen use scripts for productive, so they may write their own or
download from someone else, and copy or link the script to $HOME/bin or somewhere
list in the $PATH manually.

bmer is a simple script to manage such scripts.

- install: install the script to `$HOME/bin`

    ```sh
    $ bmer -i <script-path> [alias]
    ```

- uninstall

    ```sh
    $ bmer -r <scriptname>
    ```

- list: without any argument, list the installed script and it's path.

    ```sh
    $ bmer
    ```
