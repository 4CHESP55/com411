import basics.decisions as decisions
import basics.functions as functions
import basics.input as inputs
import basics.modules as modules
import basics.output as output
import basics.repetitions as repetitions

def run_block_a():
    print("Which module in 'Block A: Basics' do you wish to run?")
    print('''
          1. decisions
          2. functions
          3. inputs
          4. modules
          5. output
          6. repetitions
          ''')
    response = int(input())
    if response == 1:
      print('''
            1. nested_decision (dir)
            2. simple_decision (dir)
            3. and_operator
            4. or_operator
            ''')
      response = int(input())
      if response == 1:
        print('''
              1. nestception
              2. nested
              ''')
        response = int(input())
        if response == 1:
          decisions.nested_decision.nestception.run()
        elif response == 2:
          decisions.nested_decision.nested.run()
      elif response == 2:
        print('''
              1. comparison_operators
              2. counter
              3. if_elif_else
              4. if_else
              5. if_statement
              6. modulo_operator
              ''')
        response = int(input())
        if response == 1:
          decisions.simple_decision.comparison_operators.run()
        elif response == 2:
          decisions.simple_decision.counter.run()
        elif response == 3:
          decisions.simple_decision.if_elif_else.run()
        elif response == 4:
          decisions.simple_decision.if_else.run()
        elif response == 5:
          decisions.simple_decision.if_statement.run()
        elif response == 6:
          decisions.simple_decision.modulo_operator.run()
      elif response == 3:
        decisions.and_operator.run()
      elif response == 4:
        decisions.or_operator.run()
    
    elif response == 2:
      print('''
            1. acsii_character
            2. ascii_code
            3. function_calls
            4. function_with_loop
            5. function_with_nesting
            6. function_with_parameter
            7. function_with_parameters
            8. multiple_functions
            9. return_values
            10. simple_function
            ''')
      reponse = int(input())
      if reponse == 1:
        functions.acsii_character.run()
      elif response == 2:
        functions.ascii_code.run()
      elif response == 3:
        functions.function_calls.run()
      elif response == 4:
        functions.function_with_loop.run()
      elif response == 5:
        functions.function_with_nesting.run()
      elif response == 6:
        functions.function_with_parameter.run()
      elif response == 7:
        functions.function_with_parameters.run()
      elif response == 8:
        functions.multiple_functions.run()
      elif response == 9:
        functions.return_values.run()
      elif response == 10:
        functions.simple_function.run()

    elif reponse == 3:
      print('''
            1. ascii_art
            2. data_types
            3. string_operators
            4. user_input
            ''')
      reponse = int(input())
      if response == 1:
        inputs.ascii_art.run()
      elif response == 2:
        inputs.data_types.run()
      elif reponse == 3:
        inputs.string_operators.run()
      elif reponse == 4:
        inputs.user_input.run()
    
    elif response == 4:
      print('''
            1. guess_the_number
            ''')
      reponse = int(input())
      if reponse == 1:
        modules.guess_the_number.run()

    elif reponse == 5:
      print('''
            1. ascii_art
            2. escape_charaters
            3. multiline_message
            4. simple_message
            ''')
      response = int(input())
      if response == 1:
        output.ascii_art.run()
      elif reponse == 2:
        output.escape_charaters.run()
      elif reponse == 3:
        output.multiline_message.run()
      elif reponse == 4:
        output.simple_message.run()
    
    elif response == 6:
      print('''
            1. for_loop (dir)
            2. nested_loop (dir)
            3. while_loop (dir)
            ''')
      reponse = int(input())
      if response == 1:
        print('''
              1. characters
              2. count_down
              3. membership_operators
              4. range
              5. reverse
              6. simple
              ''')
        response = int(input())
        if response == 1:
          repetitions.for_loop.characters.run()
        elif response == 2:
          repetitions.for_loop.count_down.run()
        elif response == 3:
          repetitions.for_loop.membership_operators.run()
        elif response == 4:
          repetitions.for_loop.range.run()
        elif response == 5:
          repetitions.for_loop.reverse.run()
        elif response == 6:
          repetitions.for_loop.simple.run()
      elif response == 2:
        print('''
              1. nested
              2. nesting
              ''')
        reponse = int(input())
        if response == 1:
          repetitions.nested_loop.nested.run()
        elif reponse == 2:
          repetitions.nested_loop.nesting.run()
      elif response == 3:
        print('''
              1. ascii
              2. count
              3. factorial
              4. len
              5. simple
              6. sum_100
              7. sum_user_numbers
              ''')
        response = int(input())
        if response == 1:
          repetitions.while_loop.ascii.run()
        elif reponse == 2:
          repetitions.while_loop.count.run()
        elif reponse == 3:
          repetitions.while_loop.factorial.run()
        elif reponse == 4:
          repetitions.while_loop.len.run()
        elif reponse == 5:
          repetitions.while_loop.simple.run()
        elif reponse == 6:
          repetitions.while_loop.sum_100.run()
        elif reponse == 7:
          repetitions.while_loop.sum_user_numbers.run()


def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

