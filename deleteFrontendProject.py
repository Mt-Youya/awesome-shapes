import shutil
import os
import subprocess

current_dir = os.getcwd() 
items = os.listdir(current_dir)
folders = [item for item in items if os.path.isdir(os.path.join(current_dir, item))]

# print('current_dir',current_dir)
def delete_folder():
    for path in folders:
        folder_path = current_dir + "\\" + path

        print(f"path:  {folder_path}")

        if os.path.isdir(folder_path):
            node_modules_path = os.path.join(folder_path, "node_modules")
            if os.path.isdir(node_modules_path):
                try:
                    os.chdir(folder_path)
                    subprocess.Popen(
                        ["start", "cmd", "/k", "rimraf node_modules"], shell=True
                    )
                except Exception as e:
                    print("e", e)

            # try:
            #     shutil.rmtree(".git", onerror="remove_readonly")
            #     print(".git delete success")
            # except Exception as e:
            #     print(f"delete .git folder error: {e}")

            try: 
                shutil.rmtree(folder_path)
                print(f"Folder {folder_path} deleted")
            except Exception as e:
                print(f"delete folder error: {e}")


delete_folder()
