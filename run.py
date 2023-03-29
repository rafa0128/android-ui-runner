from public.Common import CaseStrategy,RunCases
import os

if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(),'case')
    cs = CaseStrategy(case_path=case_path, case_pattern='test*.py')
    cases = cs.collect_cases()
    r =  RunCases()
    result = r.run(cases)