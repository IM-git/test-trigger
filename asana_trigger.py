import json
import asana

from settings import ASANA_TOKEN

from src import AsanaData

TOKEN = ASANA_TOKEN
client = asana.Client.access_token(accessToken=ASANA_TOKEN)
client.options['client_name'] = "hello_world_python"
me = client.users.me()


def main():
    [print(x) for x in me]
    print(f"Hello world! My name is {me['name']}!")
    print(f"My email: {me['email']}")
    print(f"My photo: {me['photo']['image_21x21']}")
    print(f"My workspaces: {me['workspaces']}")


def test_delete_project():
    project_gid = '1202896578516952'  # Already deleted
    result = client.projects.delete_project(project_gid, opt_pretty=True)
    print('Deleted!!')


def test_create_project():
    team = '1202795154711346'
    workspace = '1202795154711344'
    project = {'name': 'test_im', 'workspace': workspace}
    # client.projects.create(project)
    client.projects.create_project(project)


def test_get_project():
    project_gid = '1202795250106664'
    result = client.projects.get_project(project_gid, opt_pretty=True)
    # save_file(result)
    print(json.dumps(result, indent=4, sort_keys=True))


def test_get_projects():
    result = client.projects.get_projects(workspace='1202795154711344', opt_pretty=True)
    print(result)
    [print(x) for x in result]


def test_get_tasks():
    project_gid = '1202795250106664'
    result = client.projects.tasks(project_gid)
    print(result)
    [print(x) for x in result]


def test_get_tasks_for_project():
    section_gid = '1202795250106664'
    result = client.tasks.get_tasks_for_project(section_gid, opt_pretty=True)
    print(result)
    [print(x) for x in result]


def test_get_sections():
    project_gid = '1202795250106664'
    result = client.sections.get_sections_for_project(project_gid, opt_pretty=True)
    print(result)
    [print(x) for x in result]


def test_get_section():
    section_gid = '1202795250106668'
    result = client.sections.get_section(section_gid, opt_pretty=True)
    print(result)
    # [print(x) for x in result]


def test_get_tasks_for_section():
    section_gid = '1202795250106668'
    result = client.tasks.get_tasks_for_section(section_gid, opt_pretty=True)
    print(result)
    [print(x) for x in result]


def test_get_task():
    task_gid = '1202938282753310'
    result = client.tasks.get_task(task_gid, opt_pretty=True)
    print(json.dumps(result, indent=4, sort_keys=True))
    print(result['notes'])
    # [print(x) for x in result]


def test_story():
    """Receive comments from the specified task."""
    task_gid = '1202938282753310'
    result = client.stories.get_stories_for_task(task_gid, opt_pretty=True)
    print(result)
    for res in result:
        if res['type'] == 'comment':
            print(res['text'])


if __name__ == '__main__':
    print("### _API ASANA_ ###")
    # main()
    # test_delete_project()
    # test_create_project()
    # test_get_project()
    # test_get_projects()
    # test_get_tasks()
    # test_get_tasks_for_project()
    # test_get_sections()
    # test_get_section()
    # test_get_tasks_for_section()
    # test_get_task()
    test_story()

