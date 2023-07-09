import behavioural.iterator, behavioural.observer, behavioural.strategy
import creational.builder, creational.factory, creational.singleton
import structural.adapter, structural.decorator, structural.facade
import abstract_class, interface

if __name__ == '__main__':

    print('Behavioural Patters')
    print('ITERATOR')
    behavioural.iterator.demo()
    
    print('OBSERVER')
    behavioural.observer.demo()
    
    print('STRATEGY')
    behavioural.strategy.demo()
    
    print('Creational Patters')
    print('BUILDER')
    creational.builder.demo()
    
    print('FACTORY')
    creational.factory.demo()
    
    print('SINGELTON')
    creational.singleton.demo()

    print('Stuctural Patters')
    print('ADAPTER')
    structural.adapter.demo()

    print('DECORATOR')
    structural.decorator.demo()
    
    print('FACADE')
    structural.facade.demo()


    print('Abstract Classes vs. Interfaces')
    abstract_class.demo()
    interface.demo()




