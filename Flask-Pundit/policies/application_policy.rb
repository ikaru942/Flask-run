class ApplicationPolicy
  attr_reader :user, :record

  def initialize(user, record)
    @user = user
    @record = record
  end

  def index?
    false
  end

  def show?
    scope.where(:id => record.id).exists?
  end

  def create?
    false
  end

  def new?
    create?
  end

  def update?
    false
  end

  def edit?
    update?
  end

  def destory?
    false
  end

  def scope
    pundit.policy_scope!(user, record.class)
  end

  class scope
    attr_reader :user, :policy_scope

    def initialize(user, scope)
      @user = user
      @scope = policy_scope
    end
    def resolve
      policy_scop
    end
  end
end
