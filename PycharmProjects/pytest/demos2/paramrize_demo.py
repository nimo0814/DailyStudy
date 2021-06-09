import pytest,sys
stu_info=[
    ({'name': 'zhangsan', 'id': 's001'}, {'course': 'english', 'score': 98}),
    ({'name': 'lisi', 'id': 's002'}, {'course': 'chinese', 'score': 77}),
    ({'name': 'wangwu', 'id': 's003'}, {'course': 'math', 'score': 69})
]

class TestDemo:
    """
    info和study是根据数据源里面的信息个数决定的，相当于定义了两个变量
    在代码中使用的变量必须跟parametrize里定义的变量名一致
    """
    #@pytest.mark.skip(reason='此版本暂时不测试')
    #@pytest.mark.skipif(sys.version_info<(3,8),reason='requires python3.8 or higher')
    @pytest.mark.smoke
    @pytest.mark.parametrize('info,study',stu_info)
    def test_stu(self,info,study):
        print('学生姓名：',info['name'])
        print('科目：',study['course'],'分数：',study['score'])
    def test_login(self):
        print('login')

if __name__=='__main__':
    pytest.main(['-s','paramrize_demo.py'])